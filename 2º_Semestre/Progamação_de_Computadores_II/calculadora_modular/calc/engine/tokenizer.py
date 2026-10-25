
import re

TOKEN_SPEC = [
    ("NUMBER",   r"\d+(?:\.\d+)?"),
    ("NAME",     r"[A-Za-z_]\w*"),
    ("OP",       r"[\+\-\*/\^]"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("PERCENT",  r"%"),
    ("WS",       r"\s+"),
]

TOKEN_RE = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))

def tokenize(expr: str):
    for m in TOKEN_RE.finditer(expr):
        kind = m.lastgroup
        value = m.group()
        if kind == "WS":
            continue
        yield (kind, value)
