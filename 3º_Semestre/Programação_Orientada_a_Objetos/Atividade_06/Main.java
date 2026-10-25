// ALUNOS: SAMUEL E SANDRINI

package atividadepoo;

import java.util.ArrayList;
import java.util.List;

/**
 * Classe Main
 * Ponto de entrada do sistema de funcionários para demonstrar o polimorfismo e as regras de negócio.
 */
public class Main {
    public static void main(String[] args) {
        // 1. Criar uma lista de objetos do tipo Funcionario (Polimorfismo)
        List<Funcionario> listaFuncionarios = new ArrayList<>();

        // 2. Adicionar instâncias de FuncionarioCLT e FuncionarioPJ
        // CLT com salário base de R$ 5.000,00
        listaFuncionarios.add(new FuncionarioCLT("Ana Silva (CLT)", 5000.00));
        
        // PJ com R$ 80,00 por hora e 160 horas trabalhadas
        listaFuncionarios.add(new FuncionarioPJ("Carlos Mendes (PJ)", 80.00, 160.00));
        
        // Outro CLT com salário base de R$ 3.000,00
        listaFuncionarios.add(new FuncionarioCLT("Beatriz Costa (CLT)", 3000.00));

        // 3. Percorrer a lista exibindo os dados e o salário calculado
        System.out.println("----- SISTEMA DE FUNCIONÁRIOS -----");
        for (Funcionario f : listaFuncionarios) {
            // Exibir dados (nome)
            f.exibirDados();
            
            // Calcular e exibir o salário (o método chamado depende do tipo real do objeto)
            double salarioCalculado = f.calcularSalario();
            System.out.printf("Salário Calculado: R$ %.2f%n", salarioCalculado);
            
            // 4. Verificar se o funcionário implementa a interface Bonificavel
            // Usamos 'instanceof' para checar se o objeto pode ser tratado como Bonificavel
            if (f instanceof Bonificavel) {
                // Se sim, fazemos o 'cast' para acessar o método calcularBonus()
                double bonus = ((Bonificavel) f).calcularBonus();
                System.out.printf("Bônus: R$ %.2f%n", bonus);
                System.out.printf("Total com Bônus: R$ %.2f%n", (salarioCalculado + bonus));
            }
            
            System.out.println("-----------------------------------");
        }
    }
}
