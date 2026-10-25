
from ..utils.errors import CalculatorError
from ..core import operations as op
from .parser import to_rpn

BIN_OPS = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.div,
    "^": op.pow_,
}

UFUNCS = {
    "u-": op.neg,
    "u+": op.pos,
    "percent": op.percent,
}

FUNCS = {
    "sqrt": op.sqrt,
    "inv": op.inv,
}

def evaluate(expr: str) -> float:
    if expr is None:
        raise CalculatorError("Expressão vazia.")
    expr = str(expr).strip()
    if not expr:
        return 0.0

    rpn = to_rpn(expr)
    stack = []

    for kind, val in rpn:
        if kind == "NUMBER":
            stack.append(float(val))

        elif kind == "OP":
            if len(stack) < 2:
                raise CalculatorError("Faltam operandos.")
            b = stack.pop()
            a = stack.pop()
            fn = BIN_OPS.get(val)
            if not fn:
                raise CalculatorError(f"Operador não suportado: {val}")
            stack.append(fn(a, b))

        elif kind == "UFUNC":
            if len(stack) < 1:
                raise CalculatorError("Faltam operandos para função unária.")
            a = stack.pop()
            fn = UFUNCS.get(val)
            if not fn:
                raise CalculatorError(f"Função unária não suportada: {val}")
            stack.append(fn(a))

        elif kind == "FUNC":
            if len(stack) < 1:
                raise CalculatorError("Faltam operandos para função.")
            a = stack.pop()
            fn = FUNCS.get(val)
            if not fn:
                raise CalculatorError(f"Função não suportada: {val}")
            stack.append(fn(a))

        else:
            raise CalculatorError(f"Token RPN inesperado: {kind} {val}")

    if len(stack) != 1:
        raise CalculatorError("Expressão malformada.")
    return stack[0]
