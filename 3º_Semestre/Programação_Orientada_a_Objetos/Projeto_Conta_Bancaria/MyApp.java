import java.util.Scanner;

/**
 * Classe MyApp
 * Classe principal da aplicação.
 * Responsável por iniciar o sistema e controlar o menu em loop.
 */
public class MyApp {

    public static void main(String[] args) {

        // Scanner para leitura de dados do usuário no console
        Scanner scanner = new Scanner(System.in);

        // Referência para a conta bancária (inicia sem conta criada)
        ContaBancaria conta = null;

        // Variável que armazena a opção escolhida no menu
        int opcao;

        // Loop principal do sistema (só termina quando o usuário escolher 0)
        do {
            System.out.println("\n=== MENU ===");
            System.out.println("1 - Criar cliente e conta");
            System.out.println("2 - Depositar");
            System.out.println("3 - Sacar");
            System.out.println("4 - Ver dados da conta");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            // Lê a opção digitada pelo usuário
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpa o buffer do teclado

            switch (opcao) {
                case 1:
                    // Criação do cliente e da conta
                    System.out.print("Nome do cliente: ");
                    String nome = scanner.nextLine();

                    System.out.print("CPF do cliente: ");
                    String cpf = scanner.nextLine();

                    Cliente cliente = new Cliente(nome, cpf);

                    System.out.print("Número da conta: ");
                    String numeroConta = scanner.nextLine();

                    conta = new ContaBancaria(numeroConta, cliente);
                    System.out.println("Cliente e conta criados com sucesso!");
                    break;

                case 2:
                    // Depósito
                    if (conta == null) {
                        System.out.println("Crie uma conta primeiro!");
                        break;
                    }
                    System.out.print("Valor do depósito: ");
                    double deposito = scanner.nextDouble();
                    conta.depositar(deposito);
                    break;

                case 3:
                    // Saque
                    if (conta == null) {
                        System.out.println("Crie uma conta primeiro!");
                        break;
                    }
                    System.out.print("Valor do saque: ");
                    double saque = scanner.nextDouble();
                    conta.sacar(saque);
                    break;

                case 4:
                    // Exibir dados da conta
                    if (conta == null) {
                        System.out.println("Nenhuma conta criada ainda!");
                    } else {
                        conta.mostrarDados();
                    }
                    break;

                case 0:
                    // Encerra o programa
                    System.out.println("Encerrando o sistema...");
                    break;

                default:
                    // Opção inválida
                    System.out.println("Opção inválida.");
            }

        } while (opcao != 0);

        // Fecha o Scanner ao final da execução
        scanner.close();
    }
}
