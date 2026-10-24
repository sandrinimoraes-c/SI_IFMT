
import ast
import operator as op

OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

class CalcError(Exception):
    pass

def safe_eval(expr: str) -> float:
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise CalcError("Constante inválida.")
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            left = _eval(node.left)
            right = _eval(node.right)
            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError("Divisão por zero")
            return OPS[type(node.op)](left, right)
        raise CalcError("Expressão inválida.")
    if not expr or not str(expr).strip():
        return 0
    try:
        tree = ast.parse(expr, mode="eval")
        return _eval(tree.body)
    except ZeroDivisionError:
        raise
    except Exception as e:
        raise CalcError(str(e))