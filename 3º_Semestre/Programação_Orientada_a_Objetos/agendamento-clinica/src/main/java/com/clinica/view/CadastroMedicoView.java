package com.clinica.view;

import com.clinica.dao.MedicoDAO;
import com.clinica.factory.DAOFactory;
import com.clinica.model.Medico;

import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import java.util.List;

/**
 * Tela de Cadastro de Médico. Segue exatamente o mesmo padrão de
 * CadastroPacienteView: a tela só conversa com a interface MedicoDAO,
 * nunca com SQL ou Connection diretamente.
 *
 * Devolve o conteúdo como Node (getContent()) para uso dentro de uma
 * aba da janela principal, em vez de abrir uma janela própria.
 */
public class CadastroMedicoView {

    private final MedicoDAO medicoDAO = DAOFactory.getMedicoDAO();

    private TextField txtNome;
    private TextField txtCrm;
    private TextField txtEspecialidade;
    private ListView<Medico> listaMedicos;

    public Node getContent() {
        Label titulo = new Label("Cadastro de médicos");
        titulo.getStyleClass().add("titulo-secao");

        Label lblNome = new Label("Nome");
        txtNome = new TextField();
        txtNome.setPromptText("Nome completo do médico");

        Label lblCrm = new Label("CRM");
        txtCrm = new TextField();
        txtCrm.setPromptText("CRM-MT 0000");

        Label lblEspecialidade = new Label("Especialidade");
        txtEspecialidade = new TextField();
        txtEspecialidade.setPromptText("Ex.: Cardiologia");

        Button btnSalvar = new Button("Salvar médico");
        btnSalvar.getStyleClass().add("botao-primario");

        Button btnExcluir = new Button("Excluir selecionado");
        btnExcluir.getStyleClass().add("botao-secundario");

        listaMedicos = new ListView<>();
        listaMedicos.setPrefHeight(220);
        atualizarLista();

        btnSalvar.setOnAction(e -> salvarMedico());
        btnExcluir.setOnAction(e -> excluirSelecionado());

        GridPane form = new GridPane();
        form.getStyleClass().add("cartao-formulario");
        form.setHgap(14);
        form.setVgap(10);
        form.setPadding(new Insets(20));

        form.add(lblNome, 0, 0);
        form.add(txtNome, 1, 0);
        form.add(lblCrm, 0, 1);
        form.add(txtCrm, 1, 1);
        form.add(lblEspecialidade, 0, 2);
        form.add(txtEspecialidade, 1, 2);

        HBox botoes = new HBox(10, btnSalvar, btnExcluir);

        Label lblLista = new Label("Médicos cadastrados");
        lblLista.getStyleClass().add("titulo-lista");

        VBox root = new VBox(16, titulo, form, botoes, lblLista, listaMedicos);
        root.setPadding(new Insets(24));
        return root;
    }

    private void salvarMedico() {
        try {
            if (txtNome.getText().isBlank() || txtCrm.getText().isBlank()
                    || txtEspecialidade.getText().isBlank()) {
                mostrarAlerta("Preencha todos os campos.");
                return;
            }

            Medico medico = new Medico(
                    txtNome.getText(),
                    txtCrm.getText(),
                    txtEspecialidade.getText()
            );

            medicoDAO.salvar(medico);

            limparCampos();
            atualizarLista();
            mostrarInfo("Médico salvo com sucesso!");

        } catch (Exception ex) {
            mostrarAlerta("Erro ao salvar médico: " + ex.getMessage());
        }
    }

    private void excluirSelecionado() {
        Medico selecionado = listaMedicos.getSelectionModel().getSelectedItem();
        if (selecionado == null) {
            mostrarAlerta("Selecione um médico na lista para excluir.");
            return;
        }

        medicoDAO.excluir(selecionado.getId());
        atualizarLista();
    }

    private void atualizarLista() {
        List<Medico> medicos = medicoDAO.listarTodos();
        listaMedicos.getItems().setAll(medicos);
    }

    private void limparCampos() {
        txtNome.clear();
        txtCrm.clear();
        txtEspecialidade.clear();
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
