from pyast_skill.engine import scan_source


def test_detects_md5_sha1():
    f = scan_source("import hashlib\nhashlib.md5(b'a')\nhashlib.sha1(b'a')\n")
    assert [x.rule_id for x in f] == ["PY003", "PY003"]
    assert f[0].severity == "medium"
