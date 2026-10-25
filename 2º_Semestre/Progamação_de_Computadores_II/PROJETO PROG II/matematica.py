import random
import time
import matplotlib.pyplot as plt

class MathFlow:
    def __init__(self):
        self.nivel = 1
        self.pontos = 0
        self.historico_niveis = []
        self.historico_tempos = []
        self.acertos_consecutivos = 0

    def gerar_problema(self):
        """Gera uma conta baseada no nível atual de dificuldade"""
        if self.nivel == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = '+'
            resposta = a + b
        elif self.nivel == 2:
            a, b = random.randint(10, 50), random.randint(1, 20)
            op = '-'
            resposta = a - b
        elif self.nivel == 3:
            a, b = random.randint(2, 12), random.randint(2, 12)
            op = '*'
            resposta = a * b
        else: # Nível 4+ (Modo Hard)
            a, b, c = random.randint(5, 20), random.randint(2, 10), random.randint(1, 10)
            op = 'Mix (* e +)'
            resposta = a * b + c
            return f"{a} * {b} + {c}", resposta
        
        return f"{a} {op} {b}", resposta

    def iniciar(self):
        print("--- BEM VINDO AO MATHFLOW ---")
        print("O sistema vai adaptar a dificuldade ao seu cérebro.")
        print("Digite 'sair' a qualquer momento para ver seu gráfico.")
        print("-" * 30)
        
        input("Pressione ENTER para começar...")
        
        inicio_sessao = time.time()
        
        while True:
            pergunta, resposta_certa = self.gerar_problema()
            
            print(f"\n[Nível {self.nivel}] Quanto é: {pergunta} ?")
            
            inicio_pergunta = time.time()
            resposta_usuario = input("R: ")
            tempo_gasto = time.time() - inicio_pergunta
            
            if resposta_usuario.lower() == 'sair':
                break
            
            try:
                if int(resposta_usuario) == resposta_certa:
                    print(f"✅ Correto! ({tempo_gasto:.2f} seg)")
                    self.pontos += 10 * self.nivel
                    self.acertos_consecutivos += 1
                    
                    # Lógica Adaptativa (Subir de Nível)
                    if self.acertos_consecutivos >= 3 and tempo_gasto < 5:
                        self.nivel += 1
                        self.acertos_consecutivos = 0
                        print(">>> NÍVEL AUMENTADO! <<<")
                else:
                    print(f"❌ Errado! Era {resposta_certa}.")
                    self.acertos_consecutivos = 0
                    # Lógica Adaptativa (Descer de Nível)
                    if self.nivel > 1:
                        self.nivel -= 1
                        print(">>> Dificuldade reduzida para reforço <<<")
            except ValueError:
                print("Por favor, digite apenas números.")
            
            # Guarda dados para o relatório final
            self.historico_niveis.append(self.nivel)
            self.historico_tempos.append(tempo_gasto)

        self.gerar_relatorio()

    def gerar_relatorio(self):
        print("\n--- RELATÓRIO DE DESEMPENHO ---")
        print(f"Pontuação Final: {self.pontos}")
        
        if len(self.historico_niveis) > 0:
            # Criação do Gráfico com Matplotlib
            plt.figure(figsize=(10, 5))
            
            # Gráfico de Evolução de Nível
            plt.subplot(1, 2, 1)
            plt.plot(self.historico_niveis, marker='o', color='purple')
            plt.title('Sua Adaptação de Nível')
            plt.xlabel('Questões')
            plt.ylabel('Dificuldade')
            plt.grid(True)
            
            # Gráfico de Tempo de Resposta
            plt.subplot(1, 2, 2)
            plt.bar(range(len(self.historico_tempos)), self.historico_tempos, color='orange')
            plt.title('Tempo de Raciocínio (s)')
            plt.xlabel('Questões')
            
            print("Gerando gráfico visual...")
            plt.show()
        else:
            print("Nenhum dado para gerar gráfico.")

if __name__ == "__main__":
    jogo = MathFlow()
    jogo.iniciar()