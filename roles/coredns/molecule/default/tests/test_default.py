"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/coredns")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_coredns_config(host):
    """Check CoreDNS config file"""
    f = host.file("/etc/coredns/Corefile")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        ".:1053 {\n"
        "    whoami\n"
        "    health :5380\n"
        "    errors\n"
        "    log\n"
        "}"
    )
    assert config in f.content_string


def test_coredns_service(host):
    """Check CoreDNS service"""
    s = host.service("coredns")
    assert s.is_running
    assert s.is_enabled


def test_coredns_docker_container(host):
    """Check CoreDNS docker container"""
    d = host.docker("coredns.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "coredns/coredns:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "APP_TEST_ENV=true" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "coredns" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]


def test_coredns_whoami(host):
    """Check if service shows whoami"""
    c = host.run("dig @localhost -p 1053 a whoami.example.org")
    assert c.succeeded
    print(c.stdout)
    assert "whoami.example.org.\t0\tIN\tA" in c.stdout
