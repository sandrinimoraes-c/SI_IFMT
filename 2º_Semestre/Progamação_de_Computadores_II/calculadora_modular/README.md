
# Calculadora Modular em Python

Calculadora estilo "do computador" com **GUI (Tkinter)** e **modo CLI**, organizada de forma **modular**.

## Estrutura
```
calculadora_modular/
├─ calc/
│  ├─ core/
│  │  ├─ operations.py
│  │  └─ memory.py
│  ├─ engine/
│  │  ├─ tokenizer.py
│  │  ├─ parser.py
│  │  └─ evaluator.py
│  ├─ ui/
│  │  ├─ cli.py
│  │  └─ gui.py
│  └─ utils/
│     └─ errors.py
├─ main_cli.py
└─ main_gui.py
```

## Recursos
- Operadores: `+ - * / ^`
- Parênteses `(` `)`
- Funções: `sqrt(x)`, `inv(x)`
- Unários: `-x`, `+x`
- Percentual pós-fixado: `x%` (interpretação simples `x/100`)
- Memória: `MC`, `MR`, `M+`, `M-`
- GUI: `C`, `CE`, `←`, `±`, `√`, `%`, `1/x`

> Nota: O `%` aqui é simples. A calculadora do Windows tem regras contextuais mais complexas.

## Como rodar
```bash
cd calculadora_modular
python main_gui.py   # interface gráfica
# ou
python main_cli.py   # terminal
```

Requer Python 3.8+ (Tkinter já vem no Python oficial).
