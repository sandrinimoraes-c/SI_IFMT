
from typing import Callable
from ..calc.state import CalcState
from ..calc.evaluator import safe_eval, CalcError

class Controller:
    def __init__(self, state: CalcState, on_display: Callable[[str], None]):
        self.state = state
        self.on_display = on_display

    def set_display(self, txt: str):
        self.on_display(txt)

    def press(self, key: str):
        if key == "C":
            self.state.clear_all()
            self.set_display("")
            return

        if key == "CE":
            self.state.clear_entry()
            self.set_display("")
            return

        if key == "⌫":
            self.state.backspace()
            self.set_display(self.state.expr)
            return

        if key == "=":
            expr = self.state.expr
            try:
                result = safe_eval(expr)
                if abs(result - int(result)) < 1e-12:
                    result = int(result)
                self.state.expr = str(result)
                self.set_display(self.state.expr)
            except ZeroDivisionError:
                self.state.expr = ""
                self.set_display("Erro (÷0)")
            except CalcError:
                self.state.expr = ""
                self.set_display("Erro")
            return

        if key in "+-*/%":
            if not self.state.expr:
                if key in "+-":
                    self.state.expr += key
            else:
                if self.state.expr[-1] in "+-*/%":
                    self.state.expr = self.state.expr[:-1] + key
                else:
                    self.state.expr += key
            self.set_display(self.state.expr)
            return

        self.state.expr += key
        self.set_display(self.state.expr)