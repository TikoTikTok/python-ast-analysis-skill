from .base import Finding, Rule
from .eval_exec import EvalExecRule
from .sql_concat import SqlConcatRule
from .subprocess_shell import SubprocessShellRule
from .weak_hash import WeakHashRule


def all_rules() -> list[Rule]:
    return [EvalExecRule(), SubprocessShellRule(), WeakHashRule(), SqlConcatRule()]


__all__ = ["Finding", "Rule", "all_rules"]
