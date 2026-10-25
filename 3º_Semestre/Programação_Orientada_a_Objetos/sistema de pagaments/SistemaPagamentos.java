import java.util.ArrayList;
import java.util.List;

class SistemaPagamentos {
    private List<Pagamento> pagamentos;

    public SistemaPagamentos() {
        this.pagamentos = new ArrayList<>();
    }

    public void adicionarPagamento(Pagamento pagamento) {
        pagamentos.add(pagamento);
    }

    public void processarTodos() {
        System.out.println("=== PROCESSAMENTO DOS PAGAMENTOS ===");
        for (Pagamento pagamento : pagamentos) {
            pagamento.processarPagamento();
            System.out.println();
        }
    }

    public void listarPagamentos() {
        System.out.println("=== RESUMO DOS PAGAMENTOS ===");
        for (Pagamento pagamento : pagamentos) {
            pagamento.exibirResumo();
        }
    }
}
