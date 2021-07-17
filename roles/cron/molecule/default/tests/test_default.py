"""Role testing files using testinfra"""


def test_cron_default_configuration(host):
    """Check cron default configuration"""
    f = host.file("/etc/crontab")
    assert f.is_file


def test_cron_root_configuration(host):
    """Check cron root configuration"""
    f = host.file("/var/spool/cron/crontabs/root")
    assert "SHELL=" in f.content_string
    assert "PATH=" in f.content_string
