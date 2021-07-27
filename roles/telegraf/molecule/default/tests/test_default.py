"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/telegraf")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_telegraf_service(host):
    """Check telegraf service"""
    s = host.service("telegraf")
    assert s.is_running
    assert s.is_enabled


def test_telegraf_docker_container(host):
    """Check telegraf docker container"""
    d = host.docker("telegraf.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "telegraf:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "INFLUX_SKIP_DATABASE_CREATION=true" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "telegraf" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]


def test_telegraf_metrics(host):
    """Check if service shows metric"""
    input = host.run((
        "curl --request POST --data-binary "
        "'molecule_test,host=localhost value=1 1434055562000000000' "
        "http://127.0.0.1:8080/telegraf"

    ))
    assert input.succeeded

    output = host.run("curl http://127.0.0.1:9273/metrics")
    assert output.succeeded
    assert 'molecule_test_value{host="localhost"} 1' in output.stdout
