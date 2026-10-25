import java.util.Date;

public class Emprestimo {
    private Date dataEmprestimo;
    private Date dataDevolucao;
    private Usuario usuario;
    private Exemplar exemplar;

    public Emprestimo(Date dataEmprestimo, Usuario usuario, Exemplar exemplar) {
        this.dataEmprestimo = dataEmprestimo;
        this.usuario = usuario;
        this.exemplar = exemplar;
        this.exemplar.setDisponivel(false); // Exemplar fica indisponível ao ser emprestado
    }

    public Date getDataEmprestimo() {
        return dataEmprestimo;
    }

    public void setDataEmprestimo(Date dataEmprestimo) {
        this.dataEmprestimo = dataEmprestimo;
    }

    public Date getDataDevolucao() {
        return dataDevolucao;
    }

    public void setDataDevolucao(Date dataDevolucao) {
        this.dataDevolucao = dataDevolucao;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public Exemplar getExemplar() {
        return exemplar;
    }

    public void setExemplar(Exemplar exemplar) {
        this.exemplar = exemplar;
    }

    public void registrarDevolucao() {
        this.dataDevolucao = new Date(); // Data de devolução é a data atual
        this.exemplar.setDisponivel(true); // Exemplar volta a ficar disponível
        System.out.println("Empréstimo do exemplar " + this.exemplar.getCodigo() + " devolvido por " + this.usuario.getNome());
    }
}
