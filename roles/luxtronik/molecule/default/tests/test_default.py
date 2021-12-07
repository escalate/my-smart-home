"""Role testing files using testinfra"""


def test_backup_directory(host):
    """Check backup directory"""
    b = host.file("/var/backups/luxtronik")
    assert b.is_directory
    assert b.user == "root"
    assert b.group == "root"
    assert b.mode == 0o755


def test_backup_cron_job(host):
    """Check backup cron job"""
    cmd = "/usr/local/bin/backup-luxtronik.sh"
    f = host.file("/var/spool/cron/crontabs/root").content_string
    assert cmd in f
