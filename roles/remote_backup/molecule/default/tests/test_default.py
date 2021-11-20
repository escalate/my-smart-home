"""Role testing files using testinfra"""


def test_remote_backup(host):
    """Check if the remote backup runs successfully"""
    cmd = host.run("/usr/local/bin/remote-backup.sh")
    assert cmd.succeeded


def test_remote_backup_cron_job(host):
    """Check remote backup cron job"""
    cmd = "/usr/local/bin/remote-backup.sh"
    f = host.file("/var/spool/cron/crontabs/root").content_string
    assert cmd in f
