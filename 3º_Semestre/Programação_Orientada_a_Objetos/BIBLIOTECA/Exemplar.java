public class Exemplar {
    private int codigo;
    private boolean disponivel;

    public Exemplar(int codigo) {
        this.codigo = codigo;
        this.disponivel = true; // Por padrão, um exemplar é disponível
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public boolean isDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }
}
