abstract class Pagamento {
    private int id;
    private double valor;
    private String status;
    private Cliente cliente;

    public Pagamento(int id, double valor, Cliente cliente) {
        this.id = id;
        this.valor = valor;
        this.cliente = cliente;
        this.status = "Pendente";
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public abstract void processarPagamento();

    public void exibirResumo() {
        System.out.println("Pagamento ID: " + id);
        System.out.println("Cliente: " + cliente.getNome());
        System.out.println("Valor: R$ " + String.format("%.2f", valor));
        System.out.println("Status: " + status);
    }
}
