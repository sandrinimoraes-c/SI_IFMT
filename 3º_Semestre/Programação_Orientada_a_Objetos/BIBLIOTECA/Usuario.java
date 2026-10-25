import java.util.ArrayList;
import java.util.List;

public class Usuario extends Pessoa {
    private String matricula;
    private List<Emprestimo> emprestimos;

    public Usuario(String nome, String cpf, String matricula) {
        super(nome, cpf);
        this.matricula = matricula;
        this.emprestimos = new ArrayList<>();
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public List<Emprestimo> getEmprestimos() {
        return emprestimos;
    }

    public void realizarEmprestimo(Emprestimo e) {
        this.emprestimos.add(e);
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println("Matrícula: " + this.matricula);
    }
}
