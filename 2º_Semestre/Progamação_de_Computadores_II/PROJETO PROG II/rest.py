import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading
import os

# --- Configurações de Aparência ---
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class RestauradorIA(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Restaurador de Memórias com IA")
        self.geometry("900x600")

        # --- Caminhos dos Modelos de IA (VOCÊ PRECISA BAIXAR ESTES ARQUIVOS) ---
        # Coloque-os numa pasta chamada 'models' dentro do seu projeto
        self.proto_file = 'models/colorization_deploy_v2.prototxt'
        self.model_file = 'models/colorization_release_v2.caffemodel'
        self.hull_pts_file = 'models/pts_in_hull.npy'
        self.net = None # A rede neural será carregada aqui

        self.caminho_imagem_atual = None
        
        self._configurar_interface()
        self._carregar_rede_neural_em_background()

    def _configurar_interface(self):
        # Título
        self.lbl_titulo = ctk.CTkLabel(self, text="Restaurador de Fotos P&B (Deep Learning)", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_titulo.pack(pady=20)

        # Área das Imagens (Antes e Depois)
        self.frame_imagens = ctk.CTkFrame(self)
        self.frame_imagens.pack(pady=10, expand=True, fill="both", padx=20)

        # Imagem Original (Esquerda)
        self.lbl_img_original = ctk.CTkLabel(self.frame_imagens, text="Imagem Original P&B")
        self.lbl_img_original.pack(side="left", expand=True, padx=10)

        # Imagem Colorida (Direita)
        self.lbl_img_colorida = ctk.CTkLabel(self.frame_imagens, text="Resultado da IA")
        self.lbl_img_colorida.pack(side="right", expand=True, padx=10)

        # Botões
        self.btn_carregar = ctk.CTkButton(self, text="Carregar Foto P&B", command=self.carregar_imagem, height=50, width=200)
        self.btn_carregar.pack(pady=20)
        
        self.lbl_status = ctk.CTkLabel(self, text="Carregando modelos de IA... Aguarde.", text_color="orange")
        self.lbl_status.pack(side="bottom", pady=10)

    def _carregar_rede_neural_em_background(self):
        """Carrega os arquivos pesados da IA sem travar a janela"""
        def _loader():
            try:
                # Verifica se os arquivos existem
                if not all(os.path.exists(f) for f in [self.proto_file, self.model_file, self.hull_pts_file]):
                    self.lbl_status.configure(text="ERRO: Arquivos de modelo não encontrados na pasta 'models'!", text_color="red")
                    return

                print("Carregando rede neural...")
                self.net = cv2.dnn.readNetFromCaffe(self.proto_file, self.model_file)
                pts = np.load(self.hull_pts_file)
                
                # Configurações técnicas da camada da rede
                class8 = self.net.getLayerId("class8_ab")
                conv8 = self.net.getLayerId("conv8_313_rh")
                pts = pts.transpose().reshape(2, 313, 1, 1)
                self.net.getLayer(class8).blobs = [pts.astype("float32")]
                self.net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
                
                print("IA pronta.")
                self.lbl_status.configure(text="IA Pronta! Carregue uma imagem.", text_color="green")
                self.btn_carregar.configure(state="normal")
            except Exception as e:
                 self.lbl_status.configure(text=f"Erro fatal na IA: {e}", text_color="red")
                 print(e)

        self.btn_carregar.configure(state="disabled") # Desabilita botão enquanto carrega
        threading.Thread(target=_loader, daemon=True).start()

    def carregar_imagem(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
        if file_path:
            self.caminho_imagem_atual = file_path
            self.lbl_status.configure(text="Processando... A mágica está acontecendo.", text_color="blue")
            self.mostrar_imagem(file_path, self.lbl_img_original)
            
            # Roda a colorização em outra thread para não travar
            threading.Thread(target=self.colorizar_imagem, args=(file_path,), daemon=True).start()

    def colorizar_imagem(self, path):
        try:
            # 1. Lê a imagem
            image = cv2.imread(path)
            scaled = image.astype("float32") / 255.0
            lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
            
            # 2. Separa o canal L (Luminosidade - o P&B)
            resized = cv2.resize(lab, (224, 224))
            L = cv2.split(resized)[0]
            L -= 50
            
            # 3. A MÁGICA: Pede para a IA prever as cores (canais A e B)
            self.net.setInput(cv2.dnn.blobFromImage(L))
            ab = self.net.forward()[0, :, :, :].transpose((1, 2, 0))
            
            # 4. Remonta a imagem
            ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
            L = cv2.split(lab)[0]
            colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
            
            # Converte de volta para RGB para podermos ver
            colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
            colorized = np.clip(colorized, 0, 1)
            
            # Transforma em formato que a interface entende (0-255)
            colorized = (255 * colorized).astype("uint8")
            
            # Salva temporariamente para mostrar na interface
            cv2.imwrite("temp_colorida.jpg", colorized)
            self.mostrar_imagem("temp_colorida.jpg", self.lbl_img_colorida)
            self.lbl_status.configure(text="Colorização concluída!", text_color="green")
            
        except Exception as e:
            self.lbl_status.configure(text=f"Erro ao colorizar: {e}", text_color="red")
            print(e)

    def mostrar_imagem(self, path, label_widget):
        # Função auxiliar para exibir imagens na interface CustomTkinter
        img = Image.open(path)
        # Redimensiona mantendo proporção para caber na tela
        img.thumbnail((400, 400)) 
        img_tk = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
        label_widget.configure(image=img_tk, text="") # Remove o texto e põe a imagem

if __name__ == "__main__":
    app = RestauradorIA()
    app.mainloop()