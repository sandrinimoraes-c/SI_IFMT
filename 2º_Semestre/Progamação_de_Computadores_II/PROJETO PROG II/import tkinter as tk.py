import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import threading
import PyPDF2
import nltk
import queue
import time

# --- Importações da IA de Resumo (Sumy) ---
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Configuração do NLTK (necessário para a IA entender pontuação)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

class LeitorAcessivelFinal:
    def __init__(self, root):
        self.root = root
        self.root.title("Leitor Acessível & Inteligente - IFMT")
        self.root.geometry("650x550")
        self.root.configure(bg="#f0f0f0")
        
        # --- SISTEMA DE VOZ EM SEGUNDO PLANO ---
        self.fila_de_fala = queue.Queue()
        # Inicia o "funcionário" da voz numa thread separada
        threading.Thread(target=self._worker_voz, daemon=True).start()
        
        self.texto_atual = ""
        
        # --- INTERFACE GRÁFICA ---
        
        # Cabeçalho
        tk.Label(root, text="Leitor de PDF com IA", font=("Segoe UI", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=20)
        
        self.lbl_status = tk.Label(root, text="Dica: Use a tecla TAB para navegar.", font=("Segoe UI", 12), bg="#f0f0f0", fg="#555")
        self.lbl_status.pack(pady=5)

        # Container dos Botões
        frame = tk.Frame(root, bg="#f0f0f0")
        frame.pack(pady=20)

        # --- CRIAÇÃO DOS BOTÕES ---
        
        # 1. Botão Abrir
        self.btn_abrir = tk.Button(frame, text="1. Abrir Arquivo (Espaço)", font=("Segoe UI", 14), command=self.abrir_arquivo, width=35, height=2, bg="white", relief="raised")
        self.btn_abrir.pack(pady=10)
        self.configurar_acessibilidade(self.btn_abrir, "Botão 1. Abrir Arquivo PDF. Pressione Espaço para selecionar.")

        # 2. Botão Ler Tudo
        self.btn_ler = tk.Button(frame, text="2. Ler Tudo (Espaço)", font=("Segoe UI", 14), command=self.ler_tudo, width=35, height=2, bg="white", relief="raised")
        self.btn_ler.pack(pady=10)
        self.configurar_acessibilidade(self.btn_ler, "Botão 2. Ler Texto Completo.")

        # 3. Botão Resumo IA
        self.btn_resumir = tk.Button(frame, text="3. Resumo Inteligente (Espaço)", font=("Segoe UI", 14, "bold"), bg="#0078D7", fg="white", command=self.gerar_resumo, width=35, height=2)
        self.btn_resumir.pack(pady=10)
        self.configurar_acessibilidade(self.btn_resumir, "Botão 3. Gerar Resumo com Inteligência Artificial. Ideal para textos longos.")

        # 4. Botão Parar
        self.btn_parar = tk.Button(frame, text="Parar Voz (Espaço)", font=("Segoe UI", 12), command=self.parar_fala, bg="#E81123", fg="white", width=20)
        self.btn_parar.pack(pady=20)
        self.configurar_acessibilidade(self.btn_parar, "Botão Parar Leitura.")

        # Atalhos de Teclado Globais (F1-F4)
        self.root.bind('<F1>', lambda e: self.abrir_arquivo())
        self.root.bind('<F2>', lambda e: self.ler_tudo())
        self.root.bind('<F3>', lambda e: self.gerar_resumo())
        self.root.bind('<F4>', lambda e: self.parar_fala())
        self.root.bind('<Escape>', lambda e: root.quit())

        # Focar no primeiro botão ao iniciar
        self.btn_abrir.focus_set()
        
        # Mensagem de Boas-vindas (com delay para garantir que o engine carregou)
        self.root.after(1500, lambda: self.falar("Bem vindo ao Leitor Acessível. Pressione TAB para navegar entre os botões."))

    def _worker_voz(self):
        """O motor da voz que roda sem travar a tela"""
        engine = pyttsx3.init()
        
        # Tenta configurar voz em Português
        try:
            voices = engine.getProperty('voices')
            for v in voices:
                if "brazil" in v.name.lower() or "portuguese" in v.name.lower():
                    engine.setProperty('voice', v.id)
                    break
        except: pass
        
        engine.setProperty('rate', 175) # Velocidade da fala
        
        while True:
            try:
                texto = self.fila_de_fala.get()
                
                if texto == "STOP_NOW":
                    with self.fila_de_fala.mutex:
                        self.fila_de_fala.queue.clear()
                    continue
                
                if texto:
                    print(f"Falando: {texto[:30]}...")
                    engine.say(texto)
                    engine.runAndWait()
            except:
                # Se o engine travar, recria
                engine = pyttsx3.init()

    def falar(self, texto, limpar_anterior=False):
        if limpar_anterior:
            with self.fila_de_fala.mutex:
                self.fila_de_fala.queue.clear()
            self.fila_de_fala.put("STOP_NOW")
        
        self.fila_de_fala.put(texto)

    def configurar_acessibilidade(self, widget, texto):
        # Evento <FocusIn> dispara quando o botão é selecionado pelo TAB
        widget.bind("<FocusIn>", lambda e: self.falar(texto, limpar_anterior=True))
        # Evento <Enter> dispara quando o mouse passa por cima
        widget.bind("<Enter>", lambda e: self.falar(texto, limpar_anterior=True))

    def abrir_arquivo(self):
        self.falar("Abrindo janela de seleção...", limpar_anterior=True)
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        if caminho:
            self.falar("Processando arquivo. Aguarde.")
            self.texto_atual = self.extrair_texto(caminho)
            if self.texto_atual:
                self.lbl_status.config(text="Arquivo Carregado!", fg="green")
                self.falar("Arquivo carregado com sucesso. Pressione TAB para ir para as opções de leitura.")
            else:
                self.falar("Não foi possível ler o texto deste PDF.")
        else:
             self.falar("Nenhum arquivo selecionado.")

    def extrair_texto(self, caminho):
        texto = ""
        try:
            with open(caminho, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    t = page.extract_text()
                    if t: texto += t.replace('\n', ' ') # Remove quebras de linha para fluidez
            return texto
        except: return None

    def ler_tudo(self):
        if self.texto_atual:
            self.falar("Iniciando leitura completa...", limpar_anterior=True)
            self.falar(self.texto_atual)
        else:
            self.falar("Nenhum arquivo carregado.", limpar_anterior=True)

    def gerar_resumo(self):
        if not self.texto_atual:
            self.falar("Carregue um arquivo primeiro.", limpar_anterior=True)
            return
        
        self.falar("A Inteligência Artificial está analisando o texto...", limpar_anterior=True)
        
        def _thread_calculo():
            try:
                parser = PlaintextParser.from_string(self.texto_atual, Tokenizer("portuguese"))
                summarizer = LsaSummarizer()
                # Gera resumo de 3 sentenças
                resumo = summarizer(parser.document, 3) 
                
                texto_resumo = "Aqui está o resumo dos pontos principais: "
                for sentence in resumo:
                    texto_resumo += str(sentence) + " "
                
                self.falar(texto_resumo, limpar_anterior=True)
            except Exception as e:
                print(e)
                self.falar("Ocorreu um erro ao resumir o texto.")
            
        threading.Thread(target=_thread_calculo).start()

    def parar_fala(self):
        self.falar("Leitura parada.", limpar_anterior=True)
        self.lbl_status.config(text="Parado", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LeitorAcessivelFinal(root)
    root.mainloop()