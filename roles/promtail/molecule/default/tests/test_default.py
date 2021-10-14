"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/promtail")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/promtail")
    assert d.is_directory
    assert d.user == "promtail"
    assert d.group == "root"
    assert d.mode == 0o775


def test_promtail_config(host):
    """Check Promtail config file"""
    f = host.file("/etc/promtail/config.yml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "clients:\n"
        "- url: http://loki:3100/loki/api/v1/push\n"
        "positions:\n"
        "  filename: /var/lib/promtail/positions.yaml\n"
        "scrape_configs:\n"
        "- job_name: system\n"
        "  static_configs:\n"
        "  - labels:\n"
        "      __path__: /var/log/*log\n"
        "      host: instance\n"
        "      job: varlogs\n"
        "    targets:\n"
        "    - localhost\n"
        "server:\n"
        "  grpc_listen_port: 0\n"
        "  http_listen_port: 9080"
    )
    assert config in f.content_string


def test_promtail_service(host):
    """Check Promtail service"""
    s = host.service("promtail")
    assert s.is_running
    assert s.is_enabled


def test_promtail_docker_container(host):
    """Check Promtail docker container"""
    d = host.docker("promtail.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "grafana/promtail:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "APP_TEST_ENV=true" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "promtail" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]
