package com.clinica.view;

import com.clinica.dao.PacienteDAO;
import com.clinica.factory.DAOFactory;
import com.clinica.model.Paciente;

import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import java.time.LocalDate;
import java.util.List;

/**
 * Tela de Cadastro de Paciente.
 *
 * IMPORTANTE: esta classe não tem nenhum SQL. Toda interação com o
 * banco passa pela interface PacienteDAO, obtida através da
 * DAOFactory. Isso é o requisito de "Encapsulamento de Infraestrutura"
 * do edital — a tela só fala com o DAO, nunca direto com o banco.
 *
 * Esta classe agora devolve o conteúdo como um Node (getContent()),
 * em vez de abrir sua própria janela (Stage). Isso permite que a
 * MainApp encaixe este formulário dentro de uma aba (Tab) de uma
 * única janela principal.
 */
public class CadastroPacienteView {

    // Pede o DAO para a fábrica. A tela não sabe (e não precisa saber)
    // que por trás disso existe um PacienteDAOImpl com SQL dentro.
    private final PacienteDAO pacienteDAO = DAOFactory.getPacienteDAO();

    private TextField txtNome;
    private TextField txtCpf;
    private TextField txtTelefone;
    private DatePicker dpNascimento;
    private ListView<Paciente> listaPacientes;

    /**
     * Monta o formulário e devolve o nó raiz, pronto para ser
     * colocado dentro de uma aba do TabPane na MainApp.
     */
    public Node getContent() {
        Label titulo = new Label("Cadastro de pacientes");
        titulo.getStyleClass().add("titulo-secao");

        Label lblNome = new Label("Nome");
        txtNome = new TextField();
        txtNome.setPromptText("Nome completo do paciente");

        Label lblCpf = new Label("CPF");
        txtCpf = new TextField();
        txtCpf.setPromptText("000.000.000-00");

        Label lblTelefone = new Label("Telefone");
        txtTelefone = new TextField();
        txtTelefone.setPromptText("(00) 00000-0000");

        Label lblNascimento = new Label("Data de nascimento");
        dpNascimento = new DatePicker();
        dpNascimento.setMaxWidth(Double.MAX_VALUE);

        Button btnSalvar = new Button("Salvar paciente");
        btnSalvar.getStyleClass().add("botao-primario");

        Button btnExcluir = new Button("Excluir selecionado");
        btnExcluir.getStyleClass().add("botao-secundario");

        listaPacientes = new ListView<>();
        listaPacientes.setPrefHeight(220);
        atualizarLista();

        btnSalvar.setOnAction(e -> salvarPaciente());
        btnExcluir.setOnAction(e -> excluirSelecionado());

        GridPane form = new GridPane();
        form.getStyleClass().add("cartao-formulario");
        form.setHgap(14);
        form.setVgap(10);
        form.setPadding(new Insets(20));

        form.add(lblNome, 0, 0);
        form.add(txtNome, 1, 0);
        form.add(lblCpf, 0, 1);
        form.add(txtCpf, 1, 1);
        form.add(lblTelefone, 0, 2);
        form.add(txtTelefone, 1, 2);
        form.add(lblNascimento, 0, 3);
        form.add(dpNascimento, 1, 3);

        HBox botoes = new HBox(10, btnSalvar, btnExcluir);

        Label lblLista = new Label("Pacientes cadastrados");
        lblLista.getStyleClass().add("titulo-lista");

        VBox root = new VBox(16, titulo, form, botoes, lblLista, listaPacientes);
        root.setPadding(new Insets(24));
        return root;
    }

    /**
     * Lê os campos da tela, monta um objeto Paciente e delega o
     * salvamento ao DAO. Nenhum SQL aqui — só validação simples de
     * formulário e chamada ao DAO.
     */
    private void salvarPaciente() {
        try {
            if (txtNome.getText().isBlank() || txtCpf.getText().isBlank()
                    || dpNascimento.getValue() == null) {
                mostrarAlerta("Preencha ao menos Nome, CPF e Data de Nascimento.");
                return;
            }

            LocalDate nascimento = dpNascimento.getValue();

            Paciente paciente = new Paciente(
                    txtNome.getText(),
                    txtCpf.getText(),
                    txtTelefone.getText(),
                    nascimento
            );

            pacienteDAO.salvar(paciente);

            limparCampos();
            atualizarLista();
            mostrarInfo("Paciente salvo com sucesso!");

        } catch (Exception ex) {
            mostrarAlerta("Erro ao salvar paciente: " + ex.getMessage());
        }
    }

    private void excluirSelecionado() {
        Paciente selecionado = listaPacientes.getSelectionModel().getSelectedItem();
        if (selecionado == null) {
            mostrarAlerta("Selecione um paciente na lista para excluir.");
            return;
        }

        pacienteDAO.excluir(selecionado.getId());
        atualizarLista();
    }

    private void atualizarLista() {
        List<Paciente> pacientes = pacienteDAO.listarTodos();
        listaPacientes.getItems().setAll(pacientes);
    }

    private void limparCampos() {
        txtNome.clear();
        txtCpf.clear();
        txtTelefone.clear();
        dpNascimento.setValue(null);
    }

    private void mostrarAlerta(String mensagem) {
        Alert alerta = new Alert(Alert.AlertType.WARNING, mensagem);
        alerta.showAndWait();
    }

    private void mostrarInfo(String mensagem) {
        Alert alerta = new Alert(Alert.AlertType.INFORMATION, mensagem);
        alerta.showAndWait();
    }
}
