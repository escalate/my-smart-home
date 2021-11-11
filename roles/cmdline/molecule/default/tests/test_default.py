"""Role testing files using testinfra"""


def test_cmdline_file(host):
    """Check Linux kernel command line file"""
    f = host.file("/boot/cmdline.txt")

    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
    assert (
        "console=serial0,115200 "
        "console=tty1 "
        "root=UUID=49a6dc8a-761b-418a-bb46-344127dcc1a0 "
        "rootfstype=ext4 "
        "elevator=deadline "
        "fsck.repair=yes "
        "rootwait"
    ) in f.content_string
