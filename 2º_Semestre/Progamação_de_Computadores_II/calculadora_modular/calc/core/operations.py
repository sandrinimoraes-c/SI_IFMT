
import math
from ..utils.errors import CalculatorError

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

def div(a, b):
    if b == 0:
        raise CalculatorError("Divisão por zero.")
    return a / b

def pow_(a, b):
    try:
        return a ** b
    except ValueError as e:
        raise CalculatorError(f"Potência inválida: {e}")

def neg(a): return -a
def pos(a): return +a

def sqrt(a):
    if a < 0:
        raise CalculatorError("Raiz de número negativo.")
    return math.sqrt(a)

def inv(a):
    if a == 0:
        raise CalculatorError("Inverso de zero.")
    return 1.0 / a

def percent(a):
    return a / 100.0
