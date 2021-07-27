"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/traefik")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/traefik")
    assert d.is_directory
    assert d.user == "traefik"
    assert d.group == "root"
    assert d.mode == 0o775


def test_traefik_config(host):
    """Check Traefik config file"""
    f = host.file("/etc/traefik/traefik.yml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "accessLog: {}\n"
        "api:\n"
        "  dashboard: true\n"
        "entryPoints:\n"
        "  web:\n"
        "    address: :80\n"
        "    http:\n"
        "      redirections:\n"
        "        entryPoint:\n"
        "          scheme: https\n"
        "          to: websecure\n"
        "  websecure:\n"
        "    address: :443\n"
        "global:\n"
        "  checkNewVersion: false\n"
        "  sendAnonymousUsage: false\n"
        "log:\n"
        "  level: INFO\n"
        "providers:\n"
        "  docker:\n"
        "    exposedByDefault: false\n"
    )
    assert config in f.content_string


def test_traefik_service(host):
    """Check Traefik service"""
    s = host.service("traefik")
    assert s.is_running
    assert s.is_enabled


def test_traefik_docker_container(host):
    """Check Traefik docker container"""
    d = host.docker("traefik.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "traefik:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "TRAEFIK_API_DEBUG=True" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "traefik" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]
