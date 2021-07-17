"""Role testing files using testinfra"""


def test_locale_generation(host):
    """Check locale generation"""
    f = host.file("/etc/locale.gen")
    assert f.is_file
    assert "# en_GB.UTF-8 UTF-8" not in f.content_string

    cmd = host.run("locale --all-locales")
    assert "en_GB.utf8" in cmd.stdout
