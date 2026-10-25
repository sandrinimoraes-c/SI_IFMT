package atividadepoo;

/**
 * Classe Abstrata Funcionario
 * Representa a base comum para todos os tipos de funcionários da empresa.
 * Uma classe abstrata não pode ser instanciada diretamente, apenas por meio de suas subclasses.
 */
public abstract class Funcionario {
    // Atributos protegidos para que as subclasses possam acessá-los diretamente se necessário
    protected String nome;
    protected double salarioBase;

    /**
     * Construtor da classe Funcionario.
     * @param nome O nome do funcionário.
     * @param salarioBase O salário base do funcionário.
     */
    public Funcionario(String nome, double salarioBase) {
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    /**
     * Método Abstrato calcularSalario
     * Cada tipo de funcionário terá sua própria regra de cálculo.
     * @return o salário final calculado.
     */
    public abstract double calcularSalario();

    /**
     * Método Concreto exibirDados
     * Responsável por exibir o nome do funcionário.
     */
    public void exibirDados() {
        System.out.println("Funcionário: " + nome);
    }

    // Getters para acesso controlado (boa prática em POO)
    public String getNome() {
        return nome;
    }

    public double getSalarioBase() {
        return salarioBase;
    }
}
