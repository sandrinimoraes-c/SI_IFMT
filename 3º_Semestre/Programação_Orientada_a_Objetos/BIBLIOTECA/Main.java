
import java.util.Date;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println("\n--- INICIANDO SIMULAÇÃO DO SISTEMA DE BIBLIOTECA ---\n");

        // 1. Instanciando a Biblioteca
        // Criamos a nossa biblioteca principal, dando a ela um nome e um endereço.
        Biblioteca minhaBiblioteca = new Biblioteca("Biblioteca Central IFMT", "Rua da Inovação, 123");
        System.out.println("Biblioteca '" + minhaBiblioteca.getNome() + "' criada com sucesso em " + minhaBiblioteca.getEndereco() + ".\n");

        // 2. Cadastrando Pessoas: Bibliotecário e Usuários
        // Vamos criar um bibliotecário que será responsável por algumas operações.
        Bibliotecario bibliotecario1 = new Bibliotecario("Ana Paula", "111.222.333-44", "FUNC001");
        // minhaBiblioteca.adicionarUsuario(bibliotecario1); // Removido: Biblioteca.adicionarUsuario aceita apenas Usuario, e Bibliotecario não herda de Usuario.
        System.out.println("Bibliotecário cadastrado:");
        bibliotecario1.exibirDados();
        System.out.println("\n");

        // Criamos alguns usuários que irão interagir com a biblioteca.
        Usuario usuario1 = new Usuario("Carlos Silva", "555.666.777-88", "MATR001");
        Usuario usuario2 = new Usuario("Mariana Costa", "999.888.777-66", "MATR002");
        minhaBiblioteca.adicionarUsuario(usuario1);
        minhaBiblioteca.adicionarUsuario(usuario2);

        System.out.println("Usuários cadastrados:");
        usuario1.exibirDados();
        usuario2.exibirDados();
        System.out.println("\n");

        // 3. Cadastrando Livros e Exemplares
        // O bibliotecário cadastra um novo livro no sistema.
        Livro livro1 = new Livro("Java para Iniciantes", "Autor A. Programador", "978-85-7522-000-1");
        bibliotecario1.cadastrarLivro(livro1);
        minhaBiblioteca.adicionarLivro(livro1);

        // Adicionamos exemplares a este livro. Cada exemplar tem um código único.
        livro1.adicionarExemplar(new Exemplar(101));
        livro1.adicionarExemplar(new Exemplar(102));
        livro1.adicionarExemplar(new Exemplar(103));
        System.out.println("Livro '" + livro1.getTitulo() + "' com " + livro1.getExemplares().size() + " exemplares adicionado.\n");

        Livro livro2 = new Livro("Estruturas de Dados em Java", "Autor B. Algoritmo", "978-85-7522-001-X");
        bibliotecario1.cadastrarLivro(livro2);
        minhaBiblioteca.adicionarLivro(livro2);
        livro2.adicionarExemplar(new Exemplar(201));
        livro2.adicionarExemplar(new Exemplar(202));
        System.out.println("Livro '" + livro2.getTitulo() + "' com " + livro2.getExemplares().size() + " exemplares adicionado.\n");

        // 4. Realizando Empréstimos
        System.out.println("--- REALIZANDO EMPRÉSTIMOS ---\n");

        // Usuário 1 pega um exemplar do Livro 1.
        Exemplar exemplarLivro1_1 = livro1.getExemplares().get(0);
        if (exemplarLivro1_1.isDisponivel()) {
            Emprestimo emprestimo1 = new Emprestimo(new Date(), usuario1, exemplarLivro1_1);
            usuario1.realizarEmprestimo(emprestimo1);
            System.out.println(usuario1.getNome() + " emprestou o exemplar " + exemplarLivro1_1.getCodigo() + " do livro '" + livro1.getTitulo() + "'.");
        } else {
            System.out.println("Exemplar " + exemplarLivro1_1.getCodigo() + " do livro '" + livro1.getTitulo() + "' não está disponível para empréstimo.");
        }

        // Usuário 2 pega um exemplar do Livro 2.
        Exemplar exemplarLivro2_1 = livro2.getExemplares().get(0);
        if (exemplarLivro2_1.isDisponivel()) {
            Emprestimo emprestimo2 = new Emprestimo(new Date(), usuario2, exemplarLivro2_1);
            usuario2.realizarEmprestimo(emprestimo2);
            System.out.println(usuario2.getNome() + " emprestou o exemplar " + exemplarLivro2_1.getCodigo() + " do livro '" + livro2.getTitulo() + "'.");
        } else {
            System.out.println("Exemplar " + exemplarLivro2_1.getCodigo() + " do livro '" + livro2.getTitulo() + "' não está disponível para empréstimo.");
        }

        // Tentativa de emprestar um exemplar já emprestado (Livro 1, exemplar 101)
        System.out.println("\nTentando emprestar o mesmo exemplar novamente...");
        if (exemplarLivro1_1.isDisponivel()) {
            Emprestimo emprestimoFalho = new Emprestimo(new Date(), usuario2, exemplarLivro1_1);
            usuario2.realizarEmprestimo(emprestimoFalho);
            System.out.println(usuario2.getNome() + " emprestou o exemplar " + exemplarLivro1_1.getCodigo() + " do livro '" + livro1.getTitulo() + "'.");
        } else {
            System.out.println("Exemplar " + exemplarLivro1_1.getCodigo() + " do livro '" + livro1.getTitulo() + "' NÃO está disponível para empréstimo. (Correto!)\n");
        }

        // 5. Verificando Status dos Exemplares
        System.out.println("--- VERIFICANDO STATUS DOS EXEMPLARES ---\n");
        System.out.println("Status do exemplar " + exemplarLivro1_1.getCodigo() + " (Livro 1): " + (exemplarLivro1_1.isDisponivel() ? "Disponível" : "Emprestado"));
        System.out.println("Status do exemplar " + livro1.getExemplares().get(1).getCodigo() + " (Livro 1): " + (livro1.getExemplares().get(1).isDisponivel() ? "Disponível" : "Emprestado"));
        System.out.println("Status do exemplar " + exemplarLivro2_1.getCodigo() + " (Livro 2): " + (exemplarLivro2_1.isDisponivel() ? "Disponível" : "Emprestado"));
        System.out.println("\n");

        // 6. Registrando Devoluções
        System.out.println("--- REGISTRANDO DEVOLUÇÕES ---\n");

        // Usuário 1 devolve o livro.
        List<Emprestimo> emprestimosUsuario1 = usuario1.getEmprestimos();
        if (!emprestimosUsuario1.isEmpty()) {
            Emprestimo ultimoEmprestimoUsuario1 = emprestimosUsuario1.get(0);
            ultimoEmprestimoUsuario1.registrarDevolucao();
            System.out.println("Após devolução, status do exemplar " + ultimoEmprestimoUsuario1.getExemplar().getCodigo() + ": " + (ultimoEmprestimoUsuario1.getExemplar().isDisponivel() ? "Disponível" : "Emprestado"));
        }
        System.out.println("\n");

        // 7. Exibindo Dados da Biblioteca e de Usuários
        System.out.println("--- DADOS GERAIS ---\n");
        System.out.println("Livros na biblioteca '" + minhaBiblioteca.getNome() + "':");
        for (Livro l : minhaBiblioteca.getLivros()) {
            System.out.println("- " + l.getTitulo() + " (ISBN: " + l.getIsbn() + ") com " + l.getExemplares().size() + " exemplares.");
        }
        System.out.println("\n");

        System.out.println("Usuários registrados na biblioteca:");
        for (Usuario u : minhaBiblioteca.getUsuarios()) {
            u.exibirDados();
            System.out.println("  Empréstimos ativos: " + u.getEmprestimos().stream().filter(e -> e.getDataDevolucao() == null).count());
        }
        System.out.println("\n--- SIMULAÇÃO CONCLUÍDA ---\n");
    }
}
