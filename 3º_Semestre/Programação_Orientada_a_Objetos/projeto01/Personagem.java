public class Personagem {
    // Atributos
    String nome;
    int nivel;
    int vida;
    int forca;


    // Construtor 
    public Personagem(String nome, int vida, int forca){
        this.nome = nome;
        this.vida = vida;
        this.forca = forca;
    }

    // Metodos 
    void atacar (){
        System.out.println(nome + " atacou!");
    }

    void receberDano (int dano){
        vida -= dano;
    }
}



//clase - instancia - objeto - atributo - metodos - metodo especial construtor