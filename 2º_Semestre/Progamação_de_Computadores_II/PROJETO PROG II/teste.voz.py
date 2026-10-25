import pyttsx3

print("Iniciando teste de som...")
try:
    # Força o driver do Windows (SAPI5)
    engine = pyttsx3.init('sapi5')
    
    # Tenta falar
    engine.say("Teste de som. Um, dois, três.")
    engine.runAndWait()
    
    print("O computador falou?")
except Exception as e:
    print(f"ERRO: {e}")