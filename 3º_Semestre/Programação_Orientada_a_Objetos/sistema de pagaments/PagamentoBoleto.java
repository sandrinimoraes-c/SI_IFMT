class PagamentoBoleto extends Pagamento {
    private String codigoBarras;
    private String dataVencimento;

    public PagamentoBoleto(int id, double valor, Cliente cliente, String codigoBarras, String dataVencimento) {
        super(id, valor, cliente);
        this.codigoBarras = codigoBarras;
        this.dataVencimento = dataVencimento;
    }

    public String getCodigoBarras() {
        return codigoBarras;
    }

    public void setCodigoBarras(String codigoBarras) {
        this.codigoBarras = codigoBarras;
    }

    public String getDataVencimento() {
        return dataVencimento;
    }

    public void setDataVencimento(String dataVencimento) {
        this.dataVencimento = dataVencimento;
    }

    @Override
    public void processarPagamento() {
        System.out.println("Processando pagamento por boleto de código " + codigoBarras + "...");
        setStatus("Boleto registrado");
    }

    @Override
    public void exibirResumo() {
        super.exibirResumo();
        System.out.println("Tipo: Boleto");
        System.out.println("Código de barras: " + codigoBarras);
        System.out.println("Vencimento: " + dataVencimento);
        System.out.println();
    }
}
