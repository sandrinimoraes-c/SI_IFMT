import cv2
import datetime
import os
import time

# --- CONFIGURAÇÕES ---
WEBCAM_ID = 0 
AREA_MINIMA_MOVIMENTO = 1500 # Aumentei um pouco para evitar falsos positivos
PASTA_FOTOS = "invasores"

def iniciar_sentinela():
    # Cria a pasta para salvar as fotos se ela não existir
    if not os.path.exists(PASTA_FOTOS):
        os.makedirs(PASTA_FOTOS)

    video = cv2.VideoCapture(WEBCAM_ID)
    
    print("Ajustando câmera... aguarde 2 segundos.")
    time.sleep(2) # Pausa técnica para a câmera focar
    
    # Leitura do Frame Base (Cenário Vazio)
    check, frame_inicial = video.read()
    if not check:
        print("Erro ao acessar a câmera!")
        return

    # Tratamento do frame base
    frame_base_cinza = cv2.cvtColor(frame_inicial, cv2.COLOR_BGR2GRAY)
    frame_base_cinza = cv2.GaussianBlur(frame_base_cinza, (21, 21), 0)
    
    print(f"SENTINELA ATIVO. Monitorando... (As fotos serão salvas na pasta '{PASTA_FOTOS}')")
    
    # Variável para controlar o "spam" de fotos (para não tirar 50 fotos iguais em 1 seg)
    ultimo_registro = 0

    while True:
        check, frame_atual = video.read()
        if not check: break

        # Mensagem padrão
        status_texto = "Monitorando..."
        cor_texto = (0, 255, 0) # Verde

        # Processamento
        frame_cinza = cv2.cvtColor(frame_atual, cv2.COLOR_BGR2GRAY)
        frame_cinza = cv2.GaussianBlur(frame_cinza, (21, 21), 0)

        diferenca = cv2.absdiff(frame_base_cinza, frame_cinza)
        _, frame_limiar = cv2.threshold(diferenca, 30, 255, cv2.THRESH_BINARY)
        frame_limiar = cv2.dilate(frame_limiar, None, iterations=2)
        
        contornos, _ = cv2.findContours(frame_limiar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        movimento_detectado = False

        for contorno in contornos:
            if cv2.contourArea(contorno) < AREA_MINIMA_MOVIMENTO:
                continue
            
            movimento_detectado = True
            (x, y, w, h) = cv2.boundingRect(contorno)
            # Desenha o retângulo no invasor
            cv2.rectangle(frame_atual, (x, y), (x + w, y + h), (0, 0, 255), 3)

        if movimento_detectado:
            status_texto = "ALERTA: INVASOR!"
            cor_texto = (0, 0, 255) # Vermelho
            
            # Lógica para salvar a foto (Cooldown de 1 segundo entre fotos)
            tempo_agora = time.time()
            if tempo_agora - ultimo_registro > 1.0:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                nome_arquivo = f"{PASTA_FOTOS}/invasao_{timestamp}.jpg"
                
                # Salva a imagem original (sem os retângulos, para prova limpa) ou com retângulos
                cv2.imwrite(nome_arquivo, frame_atual)
                print(f"Foto salva: {nome_arquivo}")
                ultimo_registro = time.time()

        # Interface
        cv2.putText(frame_atual, status_texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor_texto, 2)
        
        cv2.imshow("Sentinela - Sistema de Seguranca", frame_atual)

        # Tecla Q para sair e R para recalibrar o fundo
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            # Recalibrar o fundo (caso a luz mude)
            frame_base_cinza = frame_cinza
            print("Cenário de referência atualizado!")

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    iniciar_sentinela()