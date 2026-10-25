package atividadepoo;

/**
 * Classe FuncionarioPJ
 * Representa um funcionário contratado via Pessoa Jurídica (PJ).
 * O salário é calculado com base nas horas trabalhadas e no valor por hora.
 */
public class FuncionarioPJ extends Funcionario {
    // Atributos específicos da modalidade PJ
    private double valorHora;
    private double horasTrabalhadas;

    /**
     * Construtor da classe FuncionarioPJ.
     * @param nome O nome do funcionário.
     * @param valorHora O valor pago por hora trabalhada.
     * @param horasTrabalhadas A quantidade de horas trabalhadas no mês.
     */
    public FuncionarioPJ(String nome, double valorHora, double horasTrabalhadas) {
        // Inicializamos o salarioBase como 0, pois o cálculo será feito dinamicamente
        super(nome, 0.0);
        this.valorHora = valorHora;
        this.horasTrabalhadas = horasTrabalhadas;
    }

    /**
     * Implementação do cálculo de salário para funcionários PJ.
     * Regra: Valor por hora multiplicado pelas horas trabalhadas.
     * @return o salário calculado.
     */
    @Override
    public double calcularSalario() {
        // valorHora * horasTrabalhadas
        return this.valorHora * this.horasTrabalhadas;
    }

    // Getters e Setters específicos (opcional, mas boa prática)
    public double getValorHora() {
        return valorHora;
    }

    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    public double getHorasTrabalhadas() {
        return horasTrabalhadas;
    }

    public void setHorasTrabalhadas(double horasTrabalhadas) {
        this.horasTrabalhadas = horasTrabalhadas;
    }
}
