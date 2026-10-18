from pyast_skill.engine import scan_source


def test_detects_shell_true():
    f = scan_source("import subprocess\nsubprocess.run('ls', shell=True)\n")
    assert [x.rule_id for x in f] == ["PY002"]


def test_shell_false_ok():
    assert scan_source("import subprocess\nsubprocess.run(['ls'], shell=False)\n") == []
