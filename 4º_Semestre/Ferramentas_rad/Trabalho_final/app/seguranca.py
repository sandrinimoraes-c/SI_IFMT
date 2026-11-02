"""Hash de senhas com PBKDF2 (biblioteca padrão do Python)."""
import hashlib
import hmac
import os

ITERACOES = 200_000


def gerar_hash(senha: str) -> str:
    """Devolve 'iteracoes$salt$hash' (tudo em hexadecimal)."""
    salt = os.urandom(16)
    h = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, ITERACOES)
    return f"{ITERACOES}${salt.hex()}${h.hex()}"


def verificar_senha(senha: str, armazenado: str) -> bool:
    try:
        iteracoes, salt, h = armazenado.split("$")
        novo = hashlib.pbkdf2_hmac(
            "sha256", senha.encode("utf-8"), bytes.fromhex(salt), int(iteracoes)
        )
        return hmac.compare_digest(novo.hex(), h)
    except (ValueError, AttributeError):
        return False
