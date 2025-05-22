"""Role testing files using testinfra"""


import pytest


@pytest.mark.parametrize("config", [
    ("aliases \"/etc/aliases\""),
    ("auth \"on\""),
    ("syslog \"on\""),
    ("tls \"on\""),
    ("account \"gmail\""),
    ("host \"smtp.gmail.com\""),
    ("port \"587\""),
    ("from \"username@gmail.com\""),
    ("user \"username\""),
    ("password \"plain-text-password\""),
    ("account default :gmail")
])
def test_msmtp_config(host, config):
    """Check msmtp config file"""
    f = host.file("/etc/msmtprc")
    assert config in f.content_string


def test_msmtp_config_permissions(host):
    """Check msmtp config file permissions"""
    f = host.file("/etc/msmtprc")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640


def test_sendmail_command(host):
    """Check sendmail command"""
    f = host.file("/usr/sbin/sendmail")
    assert f.is_symlink
    assert f.linked_to == "/usr/bin/msmtp"


@pytest.mark.parametrize("config", [
    ("root: example@gmail.com"),
    ("default: example@gmail.com")
])
def test_aliases_config(host, config):
    """Check aliases config file"""
    f = host.file("/etc/aliases")
    assert config in f.content_string
