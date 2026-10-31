import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector

# Configuração do Tema
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# ----------------------------- Banco de Dados -----------------------------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "10111997"
DB_NAME = "sistema_login"

def conectar_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # Criação do banco e tabela automaticamente
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.database = DB_NAME
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        """)
        
        # Insere o usuário padrão caso a tabela esteja vazia
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", ("Sandrini", "1234"))
            conn.commit()
            
        return conn, cursor
    except mysql.connector.Error as err:
        messagebox.showerror("Erro de Conexão", f"Falha ao conectar ao MySQL:\n{err}")
        return None, None

# ------------------------------ Interface ------------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Acesso ao Sistema")
        self.root.geometry("380x460")
        self.root.resizable(False, False)
        
        # Cabeçalho
        ctk.CTkLabel(root, text="Bem-vindo", font=("Segoe UI", 24, "bold")).pack(pady=(40, 5))
        ctk.CTkLabel(root, text="Faça login para continuar", font=("Segoe UI", 13), text_color="#64748B").pack(pady=(0, 20))

        # Formulário de Login
        form = ctk.CTkFrame(root, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        form.pack(padx=30, pady=10, fill="both", expand=True)

        ctk.CTkLabel(form, text="Usuário", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(20, 5))
        self.ent_usuario = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, placeholder_text="Digite seu usuário")
        self.ent_usuario.pack(padx=25, pady=(0, 15))
        
        ctk.CTkLabel(form, text="Senha", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 5))
        self.ent_senha = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, placeholder_text="Digite sua senha", show="*")
        self.ent_senha.pack(padx=25, pady=(0, 15))

        # Link recuperar senha
        link = ctk.CTkButton(form, text="Esqueceu sua senha? Redefinir", font=("Segoe UI", 12, "underline"), fg_color="transparent", text_color="#2563EB", hover_color="#F1F5F9", cursor="hand2", command=self.abrir_redefinicao)
        link.pack(pady=(5, 15))

        # Botões de Ação
        botoes_frame = ctk.CTkFrame(root, fg_color="transparent")
        botoes_frame.pack(pady=(15, 25), fill="x", padx=30)
        
        self.btn_entrar = ctk.CTkButton(botoes_frame, text="Entrar", width=150, height=40, font=("Segoe UI", 13, "bold"), corner_radius=8, command=self.entrar)
        self.btn_entrar.pack(side="left", padx=(0, 10))
        
        btn_sair = ctk.CTkButton(botoes_frame, text="Sair", width=150, height=40, font=("Segoe UI", 13), fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1", corner_radius=8, command=root.destroy)
        btn_sair.pack(side="right")

        root.bind("<Return>", lambda e: self.entrar())
        self.ent_usuario.focus()

    # ---- Login ----
    def entrar(self):
        login = self.ent_usuario.get().strip()
        senha = self.ent_senha.get()

        if not login or not senha:
            messagebox.showwarning("Atenção", "Preencha usuário e senha.")
            return

        conn, cursor = conectar_db()
        if not conn:
            return

        cursor.execute("SELECT senha FROM usuarios WHERE login = %s", (login,))
        resultado = cursor.fetchone()

        if resultado and resultado[0] == senha:
            self.abrir_janela_principal(login, senha)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            self.ent_senha.delete(0, tk.END)
            
        cursor.close()
        conn.close()

    def abrir_janela_principal(self, login, senha):
        self.root.withdraw()
        janela = ctk.CTkToplevel(self.root)
        janela.title("Área do Sistema")
        janela.geometry("360x260")
        janela.resizable(False, False)

        ctk.CTkLabel(janela, text="Acesso Autorizado 🎉", font=("Segoe UI", 20, "bold"), text_color="#16A34A").pack(pady=(25, 15))
        
        info_frame = ctk.CTkFrame(janela, fg_color="#F8FAFC", corner_radius=10, border_width=1, border_color="#E2E8F0")
        info_frame.pack(padx=30, fill="x", pady=5)
        
        ctk.CTkLabel(info_frame, text=f"Usuário:  {login}", font=("Segoe UI", 13, "bold"), text_color="#1E293B").pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkLabel(info_frame, text=f"Senha:  {senha}", font=("Segoe UI", 13), text_color="#475569").pack(anchor="w", padx=20, pady=(0, 15))

        def fechar():
            janela.destroy()
            self.ent_usuario.delete(0, tk.END)
            self.ent_senha.delete(0, tk.END)
            self.root.deiconify()
            self.ent_usuario.focus()

        janela.protocol("WM_DELETE_WINDOW", fechar)
        
        btn_voltar = ctk.CTkButton(janela, text="Voltar para o Login", height=38, corner_radius=8, fg_color="#1E293B", hover_color="#0F172A", command=fechar)
        btn_voltar.pack(pady=20, padx=30, fill="x")

    # ---- Redefinir senha ----
    def abrir_redefinicao(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Redefinir Senha")
        janela.geometry("380x460")
        janela.resizable(False, False)
        janela.after(100, lambda: janela.focus())
        janela.grab_set()

        ctk.CTkLabel(janela, text="Recuperação de Conta", font=("Segoe UI", 20, "bold")).pack(pady=(25, 5))
        ctk.CTkLabel(janela, text="Preencha os dados para atualizar", font=("Segoe UI", 12), text_color="#64748B").pack(pady=(0, 10))

        form = ctk.CTkFrame(janela, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        form.pack(padx=30, pady=5, fill="both", expand=True)

        ctk.CTkLabel(form, text="Confirmar Usuário:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(15, 3))
        ent_user = ctk.CTkEntry(form, width=270, height=36, corner_radius=8)
        ent_user.pack(padx=25, pady=(0, 10))

        ctk.CTkLabel(form, text="Nova Senha:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 3))
        ent_nova = ctk.CTkEntry(form, width=270, height=36, corner_radius=8, show="*")
        ent_nova.pack(padx=25, pady=(0, 10))

        ctk.CTkLabel(form, text="Confirmar Nova Senha:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 3))
        ent_conf = ctk.CTkEntry(form, width=270, height=36, corner_radius=8, show="*")
        ent_conf.pack(padx=25, pady=(0, 15))

        def salvar():
            login = ent_user.get().strip()
            nova = ent_nova.get()
            conf = ent_conf.get()

            if not login or not nova or not conf:
                messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
                return

            if nova != conf:
                messagebox.showerror("Erro", "As senhas não coincidem.", parent=janela)
                return

            conn, cursor = conectar_db()
            if not conn:
                return

            # Verifica se o usuário existe
            cursor.execute("SELECT id FROM usuarios WHERE login = %s", (login,))
            if not cursor.fetchone():
                messagebox.showerror("Erro", "Usuário não encontrado.", parent=janela)
                cursor.close()
                conn.close()
                return

            # Atualiza a senha
            cursor.execute("UPDATE usuarios SET senha = %s WHERE login = %s", (nova, login))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!", parent=janela)
            janela.destroy()

        btns = ctk.CTkFrame(janela, fg_color="transparent")
        btns.pack(pady=(15, 25), fill="x", padx=30)
        
        btn_salvar = ctk.CTkButton(btns, text="Salvar", width=150, height=40, font=("Segoe UI", 13, "bold"), corner_radius=8, command=salvar)
        btn_salvar.pack(side="left", padx=(0, 10))
        
        btn_cancelar = ctk.CTkButton(btns, text="Cancelar", width=150, height=40, font=("Segoe UI", 13), fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1", corner_radius=8, command=janela.destroy)
        btn_cancelar.pack(side="right")
        
        ent_user.focus()

if __name__ == "__main__":
    # Testa/Cria a conexão inicial ao abrir o programa
    conn, cursor = conectar_db()
    if conn:
        cursor.close()
        conn.close()
        
    raiz = ctk.CTk()
    App(raiz)
    raiz.mainloop()
    
    #if __name__ == "__main__":
    # conn, cursor = conectar_db()
    # if conn:
    #     cursor.close()
    #     conn.close()
    # raiz = ctk.CTk()
    # App(raiz)
    # raiz.mainloop()