"""Role testing files using testinfra."""


def test_mount_command(host):
    """Check mount command"""
    cmd = host.run("mount.cifs -V")

    assert "mount.cifs version" in cmd.stdout
