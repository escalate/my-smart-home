"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/telegraf")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_telegraf_config(host):
    """Check Telegraf config file"""
    f = host.file("/etc/telegraf/telegraf.conf")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "[[inputs.http_listener_v2]]\n"
        "  service_address = \":8080\"\n"
        "  data_format = \"influx\"\n"
        "\n"
        "[[outputs.prometheus_client]]\n"
        "  listen = \":9273\"\n"
        "  metric_version = 2\n"
        "  flush_interval = \"10ms\"\n"
        "  flush_jitter = \"10ms\"\n"
        "  metric_batch_size = 1"
    )
    assert config in f.content_string


def test_telegraf_service(host):
    """Check Telegraf service"""
    s = host.service("telegraf")
    assert s.is_running
    assert s.is_enabled


def test_telegraf_docker_container(host):
    """Check Telegraf docker container"""
    d = host.docker("telegraf").inspect()
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
        "http://localhost:8080/telegraf"

    ))
    assert input.succeeded

    output = host.run("curl http://localhost:9273/metrics")
    assert output.succeeded
    assert 'molecule_test_value{host="localhost"} 1' in output.stdout
