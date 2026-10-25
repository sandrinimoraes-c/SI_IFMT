package atividadepoo;

/**
 * Classe FuncionarioCLT
 * Representa um funcionário regido pela Consolidação das Leis do Trabalho (CLT).
 * Implementa a interface Bonificavel, pois recebe bônus de 5%.
 */
public class FuncionarioCLT extends Funcionario implements Bonificavel {

    /**
     * Construtor da classe FuncionarioCLT.
     * @param nome O nome do funcionário.
     * @param salarioBase O salário base do funcionário.
     */
    public FuncionarioCLT(String nome, double salarioBase) {
        super(nome, salarioBase);
    }

    /**
     * Implementação do cálculo de salário para funcionários CLT.
     * Regra: Acréscimo de 10% sobre o salário base.
     * @return o salário calculado.
     */
    @Override
    public double calcularSalario() {
        // salarioBase + 10% de salarioBase
        return this.salarioBase * 1.10;
    }

    /**
     * Implementação do cálculo de bônus para funcionários CLT.
     * Regra: 5% sobre o salário calculado.
     * @return o valor do bônus calculado.
     */
    @Override
    public double calcularBonus() {
        // 5% do salário calculado
        return this.calcularSalario() * 0.05;
    }
}
