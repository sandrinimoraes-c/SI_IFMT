"""Configurações do sistema. A senha do banco vem de variável de ambiente
(não fica escrita no código nem no GitHub)."""
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = "animais_pontes_lacerda"

# Usuário administrador criado na primeira execução (troque a senha depois)
ADMIN_LOGIN = "admin"
ADMIN_SENHA_INICIAL = "admin123"
