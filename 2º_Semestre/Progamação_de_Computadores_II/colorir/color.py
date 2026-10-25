import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading
import os

# --- Aparência Moderna ---
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

class RestauradorIA(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Restaurador de Memórias com IA - IFMT")
        self.geometry("1000x650")

        # Caminhos dos modelos (Devem estar na pasta 'models')
        self.proto_file = 'models/colorization_deploy_v2.prototxt'
        self.model_file = 'models/colorization_release_v2.caffemodel'
        self.hull_pts_file = 'models/pts_in_hull.npy'
        self.net = None 

        self._montar_tela()
        
        # Carrega a IA em segundo plano para não travar o app
        self.after(100, self._carregar_ia)

    def _montar_tela(self):
        # Título
        self.lbl_titulo = ctk.CTkLabel(self, text="Restaurador de Fotos Históricas", font=ctk.CTkFont(size=24, weight="bold"))
        self.lbl_titulo.pack(pady=20)

        # Área Principal (Onde ficam as fotos)
        self.frame_fotos = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_fotos.pack(expand=True, fill="both", padx=20)

        # Coluna Esquerda (Original)
        self.frame_esq = ctk.CTkFrame(self.frame_fotos)
        self.frame_esq.pack(side="left", expand=True, fill="both", padx=10)
        ctk.CTkLabel(self.frame_esq, text="Original (P&B)", font=("Arial", 16)).pack(pady=10)
        self.lbl_img_original = ctk.CTkLabel(self.frame_esq, text="")
        self.lbl_img_original.pack(expand=True)

        # Coluna Direita (Colorida)
        self.frame_dir = ctk.CTkFrame(self.frame_fotos)
        self.frame_dir.pack(side="right", expand=True, fill="both", padx=10)
        ctk.CTkLabel(self.frame_dir, text="Restaurada com IA", font=("Arial", 16), text_color="#00ff00").pack(pady=10)
        self.lbl_img_colorida = ctk.CTkLabel(self.frame_dir, text="")
        self.lbl_img_colorida.pack(expand=True)

        # Botão e Status
        self.btn_carregar = ctk.CTkButton(self, text="Escolher Foto", command=self.carregar_imagem, height=50, width=200, font=("Arial", 18), state="disabled")
        self.btn_carregar.pack(pady=20)
        
        self.lbl_status = ctk.CTkLabel(self, text="Inicializando Redes Neurais...", text_color="orange")
        self.lbl_status.pack(pady=10)

    def _carregar_ia(self):
        def _loader():
            try:
                if not os.path.exists(self.model_file):
                    self.lbl_status.configure(text="ERRO: Arquivo .caffemodel não encontrado na pasta 'models'!", text_color="red")
                    return

                # Carregamento técnico do OpenCV DNN
                self.net = cv2.dnn.readNetFromCaffe(self.proto_file, self.model_file)
                pts = np.load(self.hull_pts_file)
                
                # Configuração das camadas da rede (Black Magic do OpenCV)
                class8 = self.net.getLayerId("class8_ab")
                conv8 = self.net.getLayerId("conv8_313_rh")
                pts = pts.transpose().reshape(2, 313, 1, 1)
                self.net.getLayer(class8).blobs = [pts.astype("float32")]
                self.net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
                
                self.lbl_status.configure(text="IA Pronta para uso.", text_color="green")
                self.btn_carregar.configure(state="normal")
            except Exception as e:
                self.lbl_status.configure(text=f"Erro ao carregar IA: {e}", text_color="red")
                print(e)

        threading.Thread(target=_loader, daemon=True).start()

    def carregar_imagem(self):
        path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.jpeg")])
        if path:
            self.mostrar_na_tela(path, self.lbl_img_original)
            self.lbl_status.configure(text="Processando cores...", text_color="#3498db")
            # Roda em thread para não travar a tela
            threading.Thread(target=self.processar_colorizacao, args=(path,), daemon=True).start()

    def processar_colorizacao(self, path):
        try:
            # Lógica de Colorização (LAB Color Space)
            img = cv2.imread(path)
            scaled = img.astype("float32") / 255.0
            lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
            
            resized = cv2.resize(lab, (224, 224))
            L = cv2.split(resized)[0]
            L -= 50
            
            self.net.setInput(cv2.dnn.blobFromImage(L))
            ab = self.net.forward()[0, :, :, :].transpose((1, 2, 0))
            
            ab = cv2.resize(ab, (img.shape[1], img.shape[0]))
            L = cv2.split(lab)[0]
            colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
            
            colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
            colorized = np.clip(colorized, 0, 1)
            colorized = (255 * colorized).astype("uint8")
            
            # Salva e mostra
            cv2.imwrite("temp_result.jpg", colorized)
            self.mostrar_na_tela("temp_result.jpg", self.lbl_img_colorida)
            self.lbl_status.configure(text="Sucesso! Cores restauradas.", text_color="green")
            
        except Exception as e:
            print(e)
            self.lbl_status.configure(text="Erro ao processar imagem.", text_color="red")

    def mostrar_na_tela(self, path, label):
        img = Image.open(path)
        # Redimensiona para caber bonito na tela
        img.thumbnail((400, 400))
        img_tk = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
        label.configure(image=img_tk, text="")

if __name__ == "__main__":
    app = RestauradorIA()
    app.mainloop()