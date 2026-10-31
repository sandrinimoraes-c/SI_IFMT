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
DB_PASSWORD = "10111997" # Sua senha
DB_NAME = "sistema_login_pets"

def conectar_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.database = DB_NAME
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT NOT NULL,
                nome VARCHAR(100) NOT NULL,
                especie VARCHAR(50) NOT NULL,
                sexo VARCHAR(20) NOT NULL,
                idade VARCHAR(50) NOT NULL,
                raca VARCHAR(100) NOT NULL,
                peso VARCHAR(50) NOT NULL,
                cor VARCHAR(100) NOT NULL,
                status_vida VARCHAR(20) NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
            )
        """)
        
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
        self.root.geometry("380x520")
        self.root.resizable(False, False)
        
        ctk.CTkLabel(root, text="Bem-vindo", font=("Segoe UI", 24, "bold")).pack(pady=(40, 5))
        ctk.CTkLabel(root, text="Faça login para continuar", font=("Segoe UI", 13), text_color="#64748B").pack(pady=(0, 20))

        form = ctk.CTkFrame(root, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        form.pack(padx=30, pady=10, fill="both", expand=True)

        ctk.CTkLabel(form, text="Usuário", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(15, 5))
        self.ent_usuario = ctk.CTkEntry(form, width=270, height=40, corner_radius=8)
        self.ent_usuario.pack(padx=25, pady=(0, 10))
        
        ctk.CTkLabel(form, text="Senha", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 5))
        self.ent_senha = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, show="*")
        self.ent_senha.pack(padx=25, pady=(0, 5))

        # Botão de Redefinir Senha centralizado dentro do form
        btn_redefinir = ctk.CTkButton(form, text="Esqueceu a senha? Redefinir", fg_color="transparent", text_color="#3B82F6", hover_color="#F8FAFC", font=("Segoe UI", 11, "underline"), height=20, command=self.abrir_redefinir_senha)
        btn_redefinir.pack(pady=(0, 15))

        botoes_frame = ctk.CTkFrame(root, fg_color="transparent")
        botoes_frame.pack(pady=(10, 10), fill="x", padx=30)
        
        self.btn_entrar = ctk.CTkButton(botoes_frame, text="Entrar", width=150, height=40, font=("Segoe UI", 13, "bold"), corner_radius=8, command=self.entrar)
        self.btn_entrar.pack(side="left", padx=(0, 10))
        
        btn_sair = ctk.CTkButton(botoes_frame, text="Sair", width=150, height=40, font=("Segoe UI", 13), fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1", corner_radius=8, command=root.destroy)
        btn_sair.pack(side="right")

        # Botão de Cadastrar Usuário
        btn_cadastrar = ctk.CTkButton(root, text="Novo por aqui? Cadastre-se", fg_color="transparent", text_color="#3B82F6", hover_color="#F1F5F9", font=("Segoe UI", 12, "underline"), command=self.abrir_cadastrar_usuario)
        btn_cadastrar.pack(pady=(0, 20))

        root.bind("<Return>", lambda e: self.entrar())
        self.ent_usuario.focus()

    def abrir_cadastrar_usuario(self):
        janela_cad = ctk.CTkToplevel(self.root)
        janela_cad.title("Cadastrar Usuário")
        janela_cad.geometry("350x400")
        janela_cad.resizable(False, False)
        janela_cad.focus_force()
        janela_cad.grab_set()

        ctk.CTkLabel(janela_cad, text="Novo Usuário", font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

        ctk.CTkLabel(janela_cad, text="Novo Login", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30, pady=(10, 0))
        ent_usr = ctk.CTkEntry(janela_cad, width=290, height=35)
        ent_usr.pack(padx=30, pady=(0, 10))

        ctk.CTkLabel(janela_cad, text="Senha", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30)
        ent_senha = ctk.CTkEntry(janela_cad, width=290, height=35, show="*")
        ent_senha.pack(padx=30, pady=(0, 10))

        ctk.CTkLabel(janela_cad, text="Confirmar Senha", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30)
        ent_confirma = ctk.CTkEntry(janela_cad, width=290, height=35, show="*")
        ent_confirma.pack(padx=30, pady=(0, 20))

        def salvar_usuario():
            usuario = ent_usr.get().strip()
            senha = ent_senha.get()
            confirma = ent_confirma.get()

            if not usuario or not senha or not confirma:
                messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela_cad)
                return
            
            if senha != confirma:
                messagebox.showerror("Erro", "As senhas não coincidem.", parent=janela_cad)
                return

            conn, cursor = conectar_db()
            if not conn:
                return

            try:
                cursor.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", (usuario, senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso! Faça login.", parent=janela_cad)
                janela_cad.destroy()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Erro", "Este nome de usuário já existe.", parent=janela_cad)
            
            cursor.close()
            conn.close()

        ctk.CTkButton(janela_cad, text="Cadastrar", width=290, height=40, font=("Segoe UI", 13, "bold"), command=salvar_usuario).pack(padx=30)

    def abrir_redefinir_senha(self):
        janela_senha = ctk.CTkToplevel(self.root)
        janela_senha.title("Redefinir Senha")
        janela_senha.geometry("350x400")
        janela_senha.resizable(False, False)
        janela_senha.focus_force()
        janela_senha.grab_set()

        ctk.CTkLabel(janela_senha, text="Nova Senha", font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

        ctk.CTkLabel(janela_senha, text="Usuário", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30, pady=(10, 0))
        ent_usr = ctk.CTkEntry(janela_senha, width=290, height=35)
        ent_usr.pack(padx=30, pady=(0, 10))

        ctk.CTkLabel(janela_senha, text="Senha Atual", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30)
        ent_atual = ctk.CTkEntry(janela_senha, width=290, height=35, show="*")
        ent_atual.pack(padx=30, pady=(0, 10))

        ctk.CTkLabel(janela_senha, text="Nova Senha", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=30)
        ent_nova = ctk.CTkEntry(janela_senha, width=290, height=35, show="*")
        ent_nova.pack(padx=30, pady=(0, 20))

        def salvar_senha():
            usuario = ent_usr.get().strip()
            senha_atual = ent_atual.get()
            nova_senha = ent_nova.get()

            if not usuario or not senha_atual or not nova_senha:
                messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela_senha)
                return

            conn, cursor = conectar_db()
            if not conn:
                return

            cursor.execute("SELECT id FROM usuarios WHERE login = %s AND senha = %s", (usuario, senha_atual))
            if cursor.fetchone():
                cursor.execute("UPDATE usuarios SET senha = %s WHERE login = %s", (nova_senha, usuario))
                conn.commit()
                messagebox.showinfo("Sucesso", "Senha alterada com sucesso!", parent=janela_senha)
                janela_senha.destroy()
            else:
                messagebox.showerror("Erro", "Usuário ou senha atual incorretos.", parent=janela_senha)
            
            cursor.close()
            conn.close()

        ctk.CTkButton(janela_senha, text="Confirmar Alteração", width=290, height=40, font=("Segoe UI", 13, "bold"), command=salvar_senha).pack(padx=30)

    def entrar(self):
        login = self.ent_usuario.get().strip()
        senha = self.ent_senha.get()

        if not login or not senha:
            messagebox.showwarning("Atenção", "Preencha usuário e senha.")
            return

        conn, cursor = conectar_db()
        if not conn:
            return

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

    def abrir_janela_pets(self, login, usuario_id):
        self.root.withdraw()
        janela = ctk.CTkToplevel(self.root)
        janela.title(f"Meus Pets - Usuário: {login}")
        janela.geometry("680x700")
        janela.resizable(False, False)

        ctk.CTkLabel(janela, text=f"Cadastro de Pets ({login})", font=("Segoe UI", 20, "bold")).pack(pady=(20, 10))

        form = ctk.CTkFrame(janela, fg_color="#F8FAFC", corner_radius=10, border_width=1, border_color="#E2E8F0")
        form.pack(padx=20, fill="x", pady=5)

        ctk.CTkLabel(form, text="Nome:", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, padx=10, pady=(15, 5), sticky="e")
        ent_nome = ctk.CTkEntry(form, width=180)
        ent_nome.grid(row=0, column=1, padx=10, pady=(15, 5), sticky="w")

        ctk.CTkLabel(form, text="Espécie:", font=("Segoe UI", 12, "bold")).grid(row=0, column=2, padx=10, pady=(15, 5), sticky="e")
        ent_especie = ctk.CTkOptionMenu(form, values=["Cachorro", "Gato", "Pássaro", "Outro"], width=180)
        ent_especie.grid(row=0, column=3, padx=10, pady=(15, 5), sticky="w")

        ctk.CTkLabel(form, text="Sexo:", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        ent_sexo = ctk.CTkOptionMenu(form, values=["Macho", "Fêmea"], width=180)
        ent_sexo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Idade:", font=("Segoe UI", 12, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky="e")
        ent_idade = ctk.CTkEntry(form, width=180)
        ent_idade.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Raça:", font=("Segoe UI", 12, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        ent_raca = ctk.CTkEntry(form, width=180)
        ent_raca.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Peso:", font=("Segoe UI", 12, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky="e")
        ent_peso = ctk.CTkEntry(form, width=180)
        ent_peso.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        ctk.CTkLabel(form, text="Cor:", font=("Segoe UI", 12, "bold")).grid(row=3, column=0, padx=10, pady=(5, 15), sticky="e")
        ent_cor = ctk.CTkEntry(form, width=180)
        ent_cor.grid(row=3, column=1, padx=10, pady=(5, 15), sticky="w")

        ctk.CTkLabel(form, text="Status:", font=("Segoe UI", 12, "bold")).grid(row=3, column=2, padx=10, pady=(5, 15), sticky="e")
        ent_status = ctk.CTkOptionMenu(form, values=["Vivo", "Morto"], width=180)
        ent_status.grid(row=3, column=3, padx=10, pady=(5, 15), sticky="w")

        lista_frame = ctk.CTkScrollableFrame(janela, fg_color="#FFFFFF", border_width=1, border_color="#E2E8F0")
        lista_frame.pack(padx=20, pady=15, fill="both", expand=True)

        def carregar_pets():
            for widget in lista_frame.winfo_children():
                widget.destroy()
                
            conn, cursor = conectar_db()
            if conn:
                cursor.execute("SELECT nome, especie, sexo, idade, raca, peso, cor, status_vida FROM pets WHERE usuario_id = %s", (usuario_id,))
                pets = cursor.fetchall()
                
                if not pets:
                    ctk.CTkLabel(lista_frame, text="Nenhum pet cadastrado.", text_color="#94A3B8").pack(pady=20)
                else:
                    for pet in pets:
                        status_icone = "🐾" if pet[7] == "Vivo" else "🖤"
                        texto_pet = f"{status_icone} {pet[0]} ({pet[1]} | {pet[2]}) | Idade: {pet[3]} | Raça: {pet[4]} | Peso: {pet[5]} | Cor: {pet[6]} | Status: {pet[7]}"
                        card = ctk.CTkFrame(lista_frame, fg_color="#F1F5F9", corner_radius=8)
                        card.pack(fill="x", padx=10, pady=5)
                        ctk.CTkLabel(card, text=texto_pet, font=("Segoe UI", 12)).pack(anchor="w", padx=15, pady=10)
                        
                cursor.close()
                conn.close()

        def salvar_pet():
            nome = ent_nome.get().strip()
            especie = ent_especie.get()
            sexo = ent_sexo.get()
            idade = ent_idade.get().strip()
            raca = ent_raca.get().strip()
            peso = ent_peso.get().strip()
            cor = ent_cor.get().strip()
            status_vida = ent_status.get()

            if not all([nome, especie, sexo, idade, raca, peso, cor, status_vida]):
                messagebox.showwarning("Atenção", "Preencha todos os campos do Pet.", parent=janela)
                return

            conn, cursor = conectar_db()
            if conn:
                cursor.execute("""
                    INSERT INTO pets (usuario_id, nome, especie, sexo, idade, raca, peso, cor, status_vida) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (usuario_id, nome, especie, sexo, idade, raca, peso, cor, status_vida))
                conn.commit()
                cursor.close()
                conn.close()
                
                for ent in (ent_nome, ent_idade, ent_raca, ent_peso, ent_cor):
                    ent.delete(0, tk.END)
                ent_especie.set("Cachorro")
                ent_sexo.set("Macho")
                ent_status.set("Vivo")
                
                carregar_pets()
                messagebox.showinfo("Sucesso", "Pet cadastrado com sucesso!", parent=janela)

        btn_salvar = ctk.CTkButton(janela, text="Salvar Pet", font=("Segoe UI", 13, "bold"), height=35, command=salvar_pet)
        btn_salvar.pack(padx=20, fill="x")

        def fechar():
            janela.destroy()
            self.ent_usuario.delete(0, tk.END)
            self.ent_senha.delete(0, tk.END)
            self.root.deiconify()
            self.ent_usuario.focus()

        janela.protocol("WM_DELETE_WINDOW", fechar)
        btn_voltar = ctk.CTkButton(janela, text="Sair da Conta", height=35, fg_color="#EF4444", hover_color="#DC2626", command=fechar)
        btn_voltar.pack(pady=(10, 20), padx=20, fill="x")

        carregar_pets()

if __name__ == "__main__":
    conn, cursor = conectar_db()
    if conn:
        cursor.close()
        conn.close()
        
    raiz = ctk.CTk()
    App(raiz)
    raiz.mainloop()