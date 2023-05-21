""" Dialog SYSPAGER control implementation """
from dataclasses import dataclass
from .__control_template import Control

@dataclass
class Pager(Control):
    window_class: str = 'SysPager'