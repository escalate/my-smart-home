"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/loki")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/loki")
    assert d.is_directory
    assert d.user == "loki"
    assert d.group == "root"
    assert d.mode == 0o775


def test_loki_config(host):
    """Check Loki config file"""
    f = host.file("/etc/loki/local-config.yaml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"


def test_loki_service(host):
    """Check Loki service"""
    s = host.service("loki")
    assert s.is_running
    assert s.is_enabled


def test_loki_docker_container(host):
    """Check Loki docker container"""
    d = host.docker("loki").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "grafana/loki:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "APP_TEST_ENV=true" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "loki" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]
