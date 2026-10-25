
from .tokenizer import tokenize
from ..utils.errors import CalculatorError

OPERATORS = {
    "+": (1, "L"),
    "-": (1, "L"),
    "*": (2, "L"),
    "/": (2, "L"),
    "^": (3, "R"),
    "u-": (4, "R"),
    "u+": (4, "R"),
}

def to_rpn(expr: str):
    output = []
    stack = []
    prev_kind = None

    tokens = list(tokenize(expr))
    i = 0
    while i < len(tokens):
        kind, value = tokens[i]

        if kind == "NUMBER":
            output.append(("NUMBER", float(value)))
            prev_kind = kind

        elif kind == "NAME":
            name = value.lower()
            if name in ("sqrt", "inv"):
                stack.append(("FUNC", name))
            else:
                raise CalculatorError(f"Função desconhecida: {value}")
            prev_kind = "FUNC"

        elif kind == "OP":
            op = value
            if prev_kind in (None, "OP", "LPAREN"):
                op = "u-" if value == "-" else ("u+" if value == "+" else value)

            while stack and stack[-1][0] in ("OP", "UFUNC"):
                top_kind, top_val = stack[-1]
                if top_kind == "UFUNC":
                    output.append(("UFUNC", top_val))
                    stack.pop()
                    continue
                p_top, assoc_top = OPERATORS[top_val]
                p_cur, assoc_cur = OPERATORS.get(op, (0, "L"))
                if (assoc_cur == "L" and p_cur <= p_top) or (assoc_cur == "R" and p_cur < p_top):
                    output.append(("OP", top_val))
                    stack.pop()
                else:
                    break
            if op not in OPERATORS:
                raise CalculatorError(f"Operador inválido: {value}")
            stack.append(("OP", op))
            prev_kind = "OP"

        elif kind == "LPAREN":
            stack.append(("LPAREN", "("))
            prev_kind = "LPAREN"

        elif kind == "RPAREN":
            while stack and stack[-1][0] != "LPAREN":
                top_kind, top_val = stack.pop()
                if top_kind in ("OP",):
                    output.append(("OP", top_val))
                elif top_kind in ("FUNC", "UFUNC"):
                    output.append((top_kind, top_val))
                else:
                    raise CalculatorError("Parênteses desbalanceados.")
            if not stack:
                raise CalculatorError("Parênteses desbalanceados.")
            stack.pop()
            if stack and stack[-1][0] == "FUNC":
                func = stack.pop()[1]
                output.append(("FUNC", func))
            prev_kind = "RPAREN"

        elif kind == "PERCENT":
            output.append(("UFUNC", "percent"))
            prev_kind = "PERCENT"

        else:
            raise CalculatorError(f"Token inesperado: {kind} {value}")

        i += 1

    while stack:
        top_kind, top_val = stack.pop()
        if top_kind == "LPAREN":
            raise CalculatorError("Parênteses desbalanceados ao final.")
        if top_kind in ("OP", "FUNC", "UFUNC"):
            output.append((top_kind, top_val))
        else:
            raise CalculatorError("Erro de pilha durante parsing.")

    return output
