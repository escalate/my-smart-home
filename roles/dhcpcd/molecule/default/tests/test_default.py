"""Role testing files using testinfra"""


import pytest


@pytest.mark.parametrize("config", [
    ("interface eth0"),
    ("static ip_address="),
    ("static routers="),
    ("static domain_name_servers="),
])
def test_dhcpcd_config(host, config):
    """Check dhcpcd config file"""
    f = host.file("/etc/dhcpcd.conf")
    assert config in f.content_string


def test_dhcpcd_config_permissions(host):
    """Check dhcpcd config file permissions"""
    f = host.file("/etc/dhcpcd.conf")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_dhcpcd_service(host):
    """Check dhcpcd service"""
    s = host.service("dhcpcd")
    assert s.is_running
    assert s.is_enabled
