
from dataclasses import dataclass

@dataclass
class CalcState:
    expr: str = ""

    def clear_all(self):
        self.expr = ""

    def clear_entry(self):
        self.expr = ""

    def backspace(self):
        self.expr = self.expr[:-1]