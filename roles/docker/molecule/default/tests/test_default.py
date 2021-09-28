"""Role testing files using testinfra"""


def test_daemon_config(host):
    """Check docker daemon config"""
    f = host.file("/etc/docker/daemon.json")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "{\n"
        "  \"live-restore\": true,\n"
        "  \"log-driver\": \"local\",\n"
        "  \"log-opts\": {\n"
        "    \"max-size\": \"100m\"\n"
        "  }\n"
        "}"
    )
    assert config in f.content_string


def test_cron_job(host):
    """Check cron job"""
    cmd = "docker system prune --all --volumes --force"
    f = host.file("/var/spool/cron/crontabs/root").content_string
    assert cmd in f


def test_docker_service(host):
    """Check docker service"""
    s = host.service("docker")
    assert s.is_running
    assert s.is_enabled
