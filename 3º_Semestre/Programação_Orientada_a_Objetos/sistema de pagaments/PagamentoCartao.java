class PagamentoCartao extends Pagamento {
    private String numeroCartao;
    private String bandeira;

    public PagamentoCartao(int id, double valor, Cliente cliente, String numeroCartao, String bandeira) {
        super(id, valor, cliente);
        this.numeroCartao = numeroCartao;
        this.bandeira = bandeira;
    }

    public String getNumeroCartao() {
        return numeroCartao;
    }

    public void setNumeroCartao(String numeroCartao) {
        this.numeroCartao = numeroCartao;
    }

    public String getBandeira() {
        return bandeira;
    }

    public void setBandeira(String bandeira) {
        this.bandeira = bandeira;
    }

    @Override
    public void processarPagamento() {
        System.out.println("Processando pagamento com cartão " + bandeira + " final " + numeroCartao + "...");
        setStatus("Aprovado no cartão");
    }

    @Override
    public void exibirResumo() {
        super.exibirResumo();
        System.out.println("Tipo: Cartão");
        System.out.println("Bandeira: " + bandeira);
        System.out.println("Cartão: **** **** **** " + numeroCartao);
        System.out.println();
    }
}
