"""Acesso ao MySQL: conexão, criação do banco e funções de consulta."""
import os

import mysql.connector

import config
from seguranca import gerar_hash, verificar_senha

CAMINHO_SCHEMA = os.path.join(os.path.dirname(__file__), "..", "banco", "schema.sql")


def conectar(com_banco: bool = True):
    parametros = {
        "host": config.DB_HOST,
        "user": config.DB_USER,
        "password": config.DB_PASSWORD,
    }
    if com_banco:
        parametros["database"] = config.DB_NAME
    return mysql.connector.connect(**parametros)


def consultar(sql: str, parametros: tuple = ()) -> list[dict]:
    """SELECT: devolve uma lista de dicionários {coluna: valor}."""
    conn = conectar()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, parametros)
        return cur.fetchall()
    finally:
        conn.close()


def executar(sql: str, parametros: tuple = ()) -> int:
    """INSERT/UPDATE/DELETE: grava e devolve o id gerado (quando houver)."""
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute(sql, parametros)
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def inicializar_banco() -> None:
    """Cria o banco e as tabelas (schema.sql) e o usuário admin, se não existirem."""
    with open(CAMINHO_SCHEMA, encoding="utf-8") as f:
        script = f.read()

    conn = conectar(com_banco=False)
    try:
        cur = conn.cursor()
        for comando in script.split(";"):
            linhas = [l for l in comando.splitlines() if not l.strip().startswith("--")]
            if "".join(linhas).strip():
                cur.execute(comando)
        conn.commit()
    finally:
        conn.close()

    if not consultar("SELECT id FROM usuarios LIMIT 1"):
        executar(
            "INSERT INTO usuarios (nome, login, senha_hash, perfil) VALUES (%s, %s, %s, 'admin')",
            ("Administrador", config.ADMIN_LOGIN, gerar_hash(config.ADMIN_SENHA_INICIAL)),
        )


def autenticar(login: str, senha: str):
    """Devolve os dados do usuário (sem o hash) ou None se login/senha estiverem errados."""
    linhas = consultar(
        "SELECT id, nome, login, senha_hash, perfil FROM usuarios WHERE login = %s AND ativo = TRUE",
        (login,),
    )
    if linhas and verificar_senha(senha, linhas[0]["senha_hash"]):
        usuario = linhas[0]
        usuario.pop("senha_hash")
        return usuario
    return None
