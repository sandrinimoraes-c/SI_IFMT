/**
 * Classe Cliente
 * Representa o cliente do banco.
 * Armazena os dados pessoais do titular da conta.
 */
public class Cliente {

    // Nome completo do cliente
    private String nome;

    // CPF do cliente
    private String cpf;

    /**
     * Construtor da classe Cliente
     * @param nome Nome do cliente
     * @param cpf CPF do cliente
     */
    public Cliente(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    /**
     * Retorna o nome do cliente
     */
    public String getNome() {
        return nome;
    }

    /**
     * Retorna o CPF do cliente
     */
    public String getCpf() {
        return cpf;
    }
}
