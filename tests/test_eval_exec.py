from pyast_skill.engine import scan_source


def test_detects_eval_and_exec():
    f = scan_source("eval('1')\nexec('x=1')\n")
    ids = [x.rule_id for x in f]
    assert ids == ["PY001", "PY001"]
    assert f[0].severity == "high" and f[0].line == 1
