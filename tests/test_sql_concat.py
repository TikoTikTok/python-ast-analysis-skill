from pyast_skill.engine import scan_source


def test_detects_fstring_sql():
    f = scan_source("cur.execute(f\"SELECT * FROM t WHERE id={uid}\")\n")
    assert [x.rule_id for x in f] == ["PY004"]
    assert f[0].severity == "high"


def test_detects_concat_sql():
    f = scan_source("cur.executemany('SELECT ' + col, rows)\n")
    assert [x.rule_id for x in f] == ["PY004"]


def test_parameterized_ok():
    assert scan_source("cur.execute('SELECT * FROM t WHERE id=?', (uid,))\n") == []
