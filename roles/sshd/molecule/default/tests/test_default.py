"""Role testing files using testinfra."""


import pytest


@pytest.mark.parametrize("config", [
    ("LogLevel INFO"),
    ("AllowGroups operator")
])
def test_sshd_config(host, config):
    """Check sshd config file"""
    f = host.file("/etc/ssh/sshd_config")
    assert config in f.content_string


def test_sshd_service(host):
    """Check sshd service"""
    s = host.service("sshd")
    assert s.is_running
    assert s.is_enabled
