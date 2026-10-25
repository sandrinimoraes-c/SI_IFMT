
from ..engine.evaluator import evaluate
from ..utils.errors import CalculatorError

BANNER = (
    "Calculadora (CLI) - digite expressões, use + - * / ^, parênteses, sqrt(), inv(), %\n"
    "Ex.: 2+2, 3*sqrt(9), 50%, 1/3, (2+3)^2\n"
    "Saia com: quit, exit ou Ctrl+C\n"
)

def repl():
    print(BANNER)
    while True:
        try:
            s = input(">> ").strip()
            if s.lower() in ("quit", "exit"):
                break
            if not s:
                continue
            try:
                res = evaluate(s)
                if abs(res - int(res)) < 1e-12:
                    print(int(res))
                else:
                    print(res)
            except CalculatorError as e:
                print(f"Erro: {e}")
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            break
