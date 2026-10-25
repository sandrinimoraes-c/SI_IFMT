class PagamentoPix extends Pagamento {
    private String chavePix;
    private String bancoOrigem;

    public PagamentoPix(int id, double valor, Cliente cliente, String chavePix, String bancoOrigem) {
        super(id, valor, cliente);
        this.chavePix = chavePix;
        this.bancoOrigem = bancoOrigem;
    }

    public String getChavePix() {
        return chavePix;
    }

    public void setChavePix(String chavePix) {
        this.chavePix = chavePix;
    }

    public String getBancoOrigem() {
        return bancoOrigem;
    }

    public void setBancoOrigem(String bancoOrigem) {
        this.bancoOrigem = bancoOrigem;
    }

    @Override
    public void processarPagamento() {
        System.out.println("Processando pagamento via Pix pela chave " + chavePix + "...");
        setStatus("Aprovado via Pix");
    }

    @Override
    public void exibirResumo() {
        super.exibirResumo();
        System.out.println("Tipo: Pix");
        System.out.println("Chave Pix: " + chavePix);
        System.out.println("Banco de origem: " + bancoOrigem);
        System.out.println();
    }
}
