
import tkinter as tk
from tkinter import ttk
from ..engine.evaluator import evaluate
from ..utils.errors import CalculatorError
from ..core.memory import memory

class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora (Modular)")
        self.geometry("350x460")
        self.resizable(False, False)

        self.expr = ""
        self.entry = ""
        self.after_eval = False

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self, padding=10)
        main.pack(fill="both", expand=True)

        self.display_var = tk.StringVar(value="0")
        display = ttk.Entry(main, textvariable=self.display_var, font=("Consolas", 22), justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=5, sticky="nsew", pady=(0,10))

        btns = [
            ("MC", self.on_mc), ("MR", self.on_mr), ("M+", self.on_mplus), ("M-", self.on_mminus), ("CE", self.on_ce),
            ("C", self.on_c), ("←", self.on_back), ("±", self.on_sign), ("√", self.on_sqrt), ("1/x", self.on_inv),
            ("7", lambda: self.on_digit("7")), ("8", lambda: self.on_digit("8")), ("9", lambda: self.on_digit("9")), ("/", lambda: self.on_op("/")), ("%", self.on_percent),
            ("4", lambda: self.on_digit("4")), ("5", lambda: self.on_digit("5")), ("6", lambda: self.on_digit("6")), ("*", lambda: self.on_op("*")), ("^", lambda: self.on_op("^")),
            ("1", lambda: self.on_digit("1")), ("2", lambda: self.on_digit("2")), ("3", lambda: self.on_digit("3")), ("-", lambda: self.on_op("-")), ("(", lambda: self.on_paren("(")),
            ("0", lambda: self.on_digit("0")), (".", lambda: self.on_dot()), (")", lambda: self.on_paren(")")), ("+", lambda: self.on_op("+")), ("=", self.on_equal),
        ]

        r = 1
        c = 0
        for text, cmd in btns:
            b = ttk.Button(main, text=text, command=cmd)
            b.grid(row=r, column=c, sticky="nsew", padx=3, pady=3, ipadx=6, ipady=8)
            c += 1
            if c == 5:
                c = 0
                r += 1

        for i in range(5):
            main.columnconfigure(i, weight=1)
        for i in range(r+1):
            main.rowconfigure(i, weight=1)

    def _update_display(self):
        if self.entry != "":
            self.display_var.set(self.entry)
        elif self.expr:
            self.display_var.set(self.expr)
        else:
            self.display_var.set("0")

    def _commit_entry(self):
        if self.entry != "":
            self.expr += self.entry
            self.entry = ""

    def on_digit(self, d):
        if self.after_eval:
            self.entry = ""
            self.expr = ""
            self.after_eval = False
        if self.entry == "0" and d == "0":
            return
        if self.entry == "0" and d != ".":
            self.entry = d
        else:
            self.entry += d
        self._update_display()

    def on_dot(self):
        if self.after_eval:
            self.entry = ""
            self.expr = ""
            self.after_eval = False
        if "." not in self.entry:
            self.entry = (self.entry or "0") + "."
            self._update_display()

    def on_op(self, op):
        if self.entry == "" and self.expr == "":
            if op in "+-":
                self.entry = op
                self._update_display()
                return
            else:
                return
        self._commit_entry()
        if self.expr and self.expr[-1] in "+-*/^":
            self.expr = self.expr[:-1] + op
        else:
            self.expr += op
        self.after_eval = False
        self._update_display()

    def on_paren(self, par):
        if par == "(":
            if self.entry != "":
                self._commit_entry()
                self.expr += "*("
            else:
                self.expr += "("
        else:
            self._commit_entry()
            self.expr += ")"
        self._update_display()

    def on_equal(self):
        self._commit_entry()
        if not self.expr:
            return
        try:
            res = evaluate(self.expr)
            txt = str(res)
            if abs(res - int(res)) < 1e-12:
                txt = str(int(res))
            self.entry = txt
            self.expr = ""
            self.after_eval = True
            self._update_display()
        except CalculatorError:
            self.entry = "Erro"
            self.expr = ""
            self.after_eval = True
            self._update_display()

    def on_c(self):
        self.expr = ""
        self.entry = ""
        self.after_eval = False
        self._update_display()

    def on_ce(self):
        self.entry = ""
        self._update_display()

    def on_back(self):
        if self.entry:
            self.entry = self.entry[:-1]
            self._update_display()

    def on_sign(self):
        if not self.entry:
            return
        if self.entry.startswith("-"):
            self.entry = self.entry[1:]
        else:
            self.entry = "-" + self.entry
        self._update_display()

    def on_sqrt(self):
        val = self.entry or "0"
        try:
            res = evaluate(f"sqrt({val})")
            self.entry = str(int(res)) if abs(res - int(res)) < 1e-12 else str(res)
            self._update_display()
        except CalculatorError:
            self.entry = "Erro"
            self.expr = ""
            self.after_eval = True
            self._update_display()

    def on_inv(self):
        val = self.entry or "0"
        try:
            res = evaluate(f"inv({val})")
            self.entry = str(int(res)) if abs(res - int(res)) < 1e-12 else str(res)
            self._update_display()
        except CalculatorError:
            self.entry = "Erro"
            self.expr = ""
            self.after_eval = True
            self._update_display()

    def on_percent(self):
        val = self.entry or "0"
        try:
            res = evaluate(f"{val}%")
            self.entry = str(int(res)) if abs(res - int(res)) < 1e-12 else str(res)
            self._update_display()
        except CalculatorError:
            self.entry = "Erro"
            self.expr = ""
            self.after_eval = True
            self._update_display()

    def on_mc(self):
        memory.clear()

    def on_mr(self):
        v = memory.recall()
        self.entry = str(int(v)) if abs(v - int(v)) < 1e-12 else str(v)
        self._update_display()

    def on_mplus(self):
        val = self.entry or "0"
        try:
            v = evaluate(val)
            memory.add(v)
        except CalculatorError:
            pass

    def on_mminus(self):
        val = self.entry or "0"
        try:
            v = evaluate(val)
            memory.sub(v)
        except CalculatorError:
            pass

def run():
    app = CalculatorGUI()
    app.mainloop()
