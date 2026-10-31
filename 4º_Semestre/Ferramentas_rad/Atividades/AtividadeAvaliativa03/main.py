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
DB_PASSWORD = "" # Coloque sua senha aqui se houver
DB_NAME = "sistema_login"

def conectar_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # Criação do banco
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.database = DB_NAME
        
        # Tabela de Usuários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        """)
        
        # Tabela de Pets (Relacionada ao Usuário)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT NOT NULL,
                nome VARCHAR(100) NOT NULL,
                idade VARCHAR(50) NOT NULL,
                raca VARCHAR(100) NOT NULL,
                peso VARCHAR(50) NOT NULL,
                cor VARCHAR(100) NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
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
        self.ent_usuario = ctk.CTkEntry(form, width=270, height=40, corner_radius=8)
        self.ent_usuario.pack(padx=25, pady=(0, 15))
        
        ctk.CTkLabel(form, text="Senha", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 5))
        self.ent_senha = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, show="*")
        self.ent_senha.pack(padx=25, pady=(0, 15))

        # Botões de Ação
        botoes_frame = ctk.CTkFrame(root, fg_color="transparent")
        botoes_frame.pack(pady=(25, 25), fill="x", padx=30)
        
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

        # Busca o ID e a senha do usuário
        cursor.execute("SELECT id, senha FROM usuarios WHERE login = %s", (login,))
        resultado = cursor.fetchone()

        if resultado and resultado[1] == senha:
            usuario_id = resultado[0]
            self.abrir_janela_pets(login, usuario_id)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            self.ent_senha.delete(0, tk.END)
            
        cursor.close()
        conn.close()

    # ---- Janela de Cadastro de Pets ----
    def abrir_janela_pets(self, login, usuario_id):
        self.root.withdraw()
        janela = ctk.CTkToplevel(self.root)
        janela.title(f"Meus Pets - Usuário: {login}")
        janela.geometry("600x650")
        janela.resizable(False, False)

        # Título
        ctk.CTkLabel(janela, text=f"Cadastro de Pets ({login})", font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

        # Frame de Formulário
        form = ctk.CTkFrame(janela, fg_color="#F8FAFC", corner_radius=10, border_width=1, border_color="#E2E8F0")
        form.pack(padx=20, fill="x", pady=5)

        # Campos em Grid (2 colunas)
        ctk.CTkLabel(form, text="Nome:", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, padx=10, pady=(15, 5), sticky="e")
        ent_nome = ctk.CTkEntry(form, width=180)
        ent_nome.grid(row=0, column=1, padx=10, pady=(15, 5), sticky="w")

        ctk.CTkLabel(form, text="Idade:", font=("Segoe UI", 12, "bold")).grid(row=0, column=2, padx=10, pady=(15, 5), sticky="e")
        ent_idade = ctk.CTkEntry(form, width=180)
        ent_idade.grid(row=0, column=3, padx=10, pady=(15, 5), sticky="w")

        ctk.CTkLabel(form, text="Raça:", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        ent_raca = ctk.CTkEntry(form, width=180)
        ent_raca.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Peso:", font=("Segoe UI", 12, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky="e")
        ent_peso = ctk.CTkEntry(form, width=180)
        ent_peso.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Cor:", font=("Segoe UI", 12, "bold")).grid(row=2, column=0, padx=10, pady=(5, 15), sticky="e")
        ent_cor = ctk.CTkEntry(form, width=180)
        ent_cor.grid(row=2, column=1, padx=10, pady=(5, 15), sticky="w")

        # Scrollable Frame para listar os Pets
        lista_frame = ctk.CTkScrollableFrame(janela, fg_color="#FFFFFF", border_width=1, border_color="#E2E8F0")
        lista_frame.pack(padx=20, pady=15, fill="both", expand=True)

        def carregar_pets():
            # Limpa a lista atual
            for widget in lista_frame.winfo_children():
                widget.destroy()
                
            conn, cursor = conectar_db()
            if conn:
                # Busca SOMENTE os pets do usuário logado
                cursor.execute("SELECT nome, idade, raca, peso, cor FROM pets WHERE usuario_id = %s", (usuario_id,))
                pets = cursor.fetchall()
                
                if not pets:
                    ctk.CTkLabel(lista_frame, text="Nenhum pet cadastrado.", text_color="#94A3B8").pack(pady=20)
                else:
                    for pet in pets:
                        texto_pet = f"🐾 {pet[0]} | Idade: {pet[1]} | Raça: {pet[2]} | Peso: {pet[3]} | Cor: {pet[4]}"
                        card = ctk.CTkFrame(lista_frame, fg_color="#F1F5F9", corner_radius=8)
                        card.pack(fill="x", padx=10, pady=5)
                        ctk.CTkLabel(card, text=texto_pet, font=("Segoe UI", 12)).pack(anchor="w", padx=15, pady=10)
                        
                cursor.close()
                conn.close()

        def salvar_pet():
            nome = ent_nome.get().strip()
            idade = ent_idade.get().strip()
            raca = ent_raca.get().strip()
            peso = ent_peso.get().strip()
            cor = ent_cor.get().strip()

            if not all([nome, idade, raca, peso, cor]):
                messagebox.showwarning("Atenção", "Preencha todos os campos do Pet.", parent=janela)
                return

            conn, cursor = conectar_db()
            if conn:
                cursor.execute("""
                    INSERT INTO pets (usuario_id, nome, idade, raca, peso, cor) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (usuario_id, nome, idade, raca, peso, cor))
                conn.commit()
                cursor.close()
                conn.close()
                
                # Limpa os campos
                for ent in (ent_nome, ent_idade, ent_raca, ent_peso, ent_cor):
                    ent.delete(0, tk.END)
                
                # Recarrega a lista
                carregar_pets()
                messagebox.showinfo("Sucesso", "Pet cadastrado com sucesso!", parent=janela)

        # Botão de Salvar Pet
        btn_salvar = ctk.CTkButton(form, text="Salvar Pet", font=("Segoe UI", 12, "bold"), command=salvar_pet)
        btn_salvar.grid(row=2, column=2, columnspan=2, padx=10, pady=(5, 15), sticky="we")

        # Botão Sair / Voltar
        def fechar():
            janela.destroy()
            self.ent_usuario.delete(0, tk.END)
            self.ent_senha.delete(0, tk.END)
            self.root.deiconify()
            self.ent_usuario.focus()

        janela.protocol("WM_DELETE_WINDOW", fechar)
        btn_voltar = ctk.CTkButton(janela, text="Sair da Conta", height=38, fg_color="#EF4444", hover_color="#DC2626", command=fechar)
        btn_voltar.pack(pady=(0, 20), padx=20, fill="x")

        # Carrega os pets ao abrir a janela
        carregar_pets()

if __name__ == "__main__":
    conn, cursor = conectar_db()
    if conn:
        cursor.close()
        conn.close()
        
    raiz = ctk.CTk()
    App(raiz)
    raiz.mainloop()