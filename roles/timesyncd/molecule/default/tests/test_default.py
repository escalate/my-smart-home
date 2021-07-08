"""Role testing files using testinfra"""

import pytest


@pytest.mark.parametrize("config", [
    (
        "NTP=0.debian.pool.ntp.org "
        "1.debian.pool.ntp.org "
        "2.debian.pool.ntp.org "
        "3.debian.pool.ntp.org"
    ),
    (
        "FallbackNTP=0.de.pool.ntp.org "
        "1.de.pool.ntp.org "
        "2.de.pool.ntp.org "
        "4.de.pool.ntp.org"
    )
])
def test_systemd_timesyncd_config(host, config):
    """Check systemd-timesyncd config file"""
    f = host.file("/etc/systemd/timesyncd.conf")
    assert config in f.content_string


def test_systemd_timesyncd_service(host):
    """Check systemd-timesyncd service"""
    s = host.service("systemd-timesyncd")
    assert s.is_running
    assert s.is_enabled
