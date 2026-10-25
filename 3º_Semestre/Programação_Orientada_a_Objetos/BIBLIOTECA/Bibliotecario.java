public class Bibliotecario extends Pessoa {
    private String codigoFuncionario;

    public Bibliotecario(String nome, String cpf, String codigoFuncionario) {
        super(nome, cpf);
        this.codigoFuncionario = codigoFuncionario;
    }

    public String getCodigoFuncionario() {
        return codigoFuncionario;
    }

    public void setCodigoFuncionario(String codigoFuncionario) {
        this.codigoFuncionario = codigoFuncionario;
    }

    public void cadastrarLivro(Livro l) {
        System.out.println("Livro " + l.getTitulo() + " cadastrado pelo bibliotecário " + this.getNome());
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println("Código de Funcionário: " + this.codigoFuncionario);
    }
}
