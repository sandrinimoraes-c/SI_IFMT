/**
 * Classe ContaBancaria
 * Representa uma conta bancária.
 * Contém as regras de negócio para movimentações financeiras.
 */
public class ContaBancaria {

    // Número identificador da conta
    private String numeroConta;

    // Saldo atual da conta
    private double saldo;

    // Cliente titular da conta
    private Cliente cliente;

    /**
     * Construtor da conta bancária
     * @param numeroConta Número da conta
     * @param cliente Cliente titular
     */
    public ContaBancaria(String numeroConta, Cliente cliente) {
        this.numeroConta = numeroConta;
        this.cliente = cliente;
        this.saldo = 0.0; // saldo inicial sempre começa zerado
    }

    /**
     * Realiza um depósito na conta
     * @param valor Valor a ser depositado
     */
    public void depositar(double valor) {
        // Verifica se o valor informado é válido
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito realizado com sucesso.");
        } else {
            System.out.println("Valor inválido para depósito.");
        }
    }

    /**
     * Realiza um saque na conta
     * @param valor Valor a ser sacado
     */
    public void sacar(double valor) {
        // Verifica se o valor é positivo e se há saldo suficiente
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
        }
    }

    /**
     * Exibe os dados da conta no console
     */
    public void mostrarDados() {
        System.out.println("\nTitular: " + cliente.getNome());
        System.out.println("CPF: " + cliente.getCpf());
        System.out.println("Conta: " + numeroConta);
        System.out.println("Saldo: R$ " + saldo);
    }

    /**
     * Retorna o número da conta
     */
    public String getNumeroConta() {
        return numeroConta;
    }
}
