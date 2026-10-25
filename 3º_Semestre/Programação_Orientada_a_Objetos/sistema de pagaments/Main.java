public class Main {
    public static void main(String[] args) {
        Cliente cliente1 = new Cliente("Ana Souza", "123.456.789-00");
        Cliente cliente2 = new Cliente("Carlos Lima", "987.654.321-00");

        Pagamento pagamento1 = new PagamentoCartao(1, 250.00, cliente1, "1234", "Visa");
        Pagamento pagamento2 = new PagamentoPix(2, 89.90, cliente1, "ana@email.com", "Banco do Brasil");
        Pagamento pagamento3 = new PagamentoBoleto(3, 430.75, cliente2, "34191.79001 01043.510047 91020.150008 2 87570026000", "15/05/2026");

        SistemaPagamentos sistema = new SistemaPagamentos();
        sistema.adicionarPagamento(pagamento1);
        sistema.adicionarPagamento(pagamento2);
        sistema.adicionarPagamento(pagamento3);

        cliente1.apresentar();
        cliente2.apresentar();
        System.out.println();

        sistema.processarTodos();
        sistema.listarPagamentos();
    }
}
