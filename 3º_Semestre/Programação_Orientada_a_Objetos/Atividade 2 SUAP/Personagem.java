public class Personagem {

    // Atributos
    String nome;
    int nivel;
    double pontosVida;
    double forca;

    // Construtor I - Iniciante
    public void Personagem(string nome){
        this.nome = nome;
        nivel = 1;
        pontosVida = 100;
        forca = 10;
    }
    // Construtor II - Avançado
    public void Personagem(String nome,, int nivel, double forca){
        pontosVida = nivel * 50;
        this.nome = nome;
        this.nivel = nivel;
        this.forca = forca;
    }

    // Métodos de Comportamento
    public void receberDano (double dano){
        pontosVida -= dano;
        if (pontosVida < 0) {
            pontosVida = 0;
            System.out.println("O personagem " + nome + "foi derrotado!");
        }
}