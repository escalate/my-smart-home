"""Role testing files using testinfra"""


def test_swap(host):
    """Check swap"""
    cmd = host.run("swapon --show")
    assert "/var/swap" not in cmd.stdout
