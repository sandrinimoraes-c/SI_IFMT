package com.clinica.view;

import com.clinica.dao.AgendamentoDAO;
import com.clinica.dao.MedicoDAO;
import com.clinica.dao.PacienteDAO;
import com.clinica.factory.DAOFactory;
import com.clinica.model.Agendamento;
import com.clinica.model.Medico;
import com.clinica.model.Paciente;

import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;

import java.time.LocalTime;
import java.util.List;

/**
 * Tela de Agendamento de Consultas.
 *
 * Cria o vínculo entre Paciente e Médico (data + hora), exigido no
 * edital. Toda a regra "não permitir dois agendamentos para o mesmo
 * médico no mesmo horário" é tratada dentro de AgendamentoDAOImpl
 * (camada de persistência) — aqui a tela apenas CAPTURA a exceção
 * lançada pelo DAO e mostra um alerta amigável ao usuário.
 *
 * Devolve o conteúdo como Node (getContent()) para uso dentro de uma
 * aba da janela principal. Também expõe atualizarCombos(), chamado
 * pela MainApp sempre que o usuário entra nesta aba — assim, se um
 * paciente ou médico novo foi cadastrado em outra aba, ele já aparece
 * na lista de seleção aqui, sem precisar reiniciar o programa.
 */
public class AgendamentoView {

    private final AgendamentoDAO agendamentoDAO = DAOFactory.getAgendamentoDAO();
    private final PacienteDAO pacienteDAO = DAOFactory.getPacienteDAO();
    private final MedicoDAO medicoDAO = DAOFactory.getMedicoDAO();

    private ComboBox<Paciente> cbPaciente;
    private ComboBox<Medico> cbMedico;
    private DatePicker dpData;
    private ComboBox<String> cbHora;
    private ListView<Agendamento> listaAgendamentos;

    public Node getContent() {
        Label titulo = new Label("Agendamento de consultas");
        titulo.getStyleClass().add("titulo-secao");

        Label lblPaciente = new Label("Paciente");
        cbPaciente = new ComboBox<>();
        cbPaciente.setMaxWidth(Double.MAX_VALUE);

        Label lblMedico = new Label("Médico");
        cbMedico = new ComboBox<>();
        cbMedico.setMaxWidth(Double.MAX_VALUE);

        Label lblData = new Label("Data da consulta");
        dpData = new DatePicker();
        dpData.setMaxWidth(Double.MAX_VALUE);

        Label lblHora = new Label("Horário");
        cbHora = new ComboBox<>();
        cbHora.setMaxWidth(Double.MAX_VALUE);
        // Horários de exemplo, de 30 em 30 minutos, das 8h às 17h30.
        for (int h = 8; h <= 17; h++) {
            cbHora.getItems().add(String.format("%02d:00", h));
            cbHora.getItems().add(String.format("%02d:30", h));
        }

        atualizarCombos();

        Button btnAgendar = new Button("Agendar consulta");
        btnAgendar.getStyleClass().add("botao-primario");

        Button btnCancelar = new Button("Cancelar selecionada");
        btnCancelar.getStyleClass().add("botao-secundario");

        listaAgendamentos = new ListView<>();
        listaAgendamentos.setPrefHeight(220);
        atualizarLista();

        btnAgendar.setOnAction(e -> agendarConsulta());
        btnCancelar.setOnAction(e -> cancelarSelecionada());

        GridPane form = new GridPane();
        form.getStyleClass().add("cartao-formulario");
        form.setHgap(14);
        form.setVgap(10);
        form.setPadding(new Insets(20));

        form.add(lblPaciente, 0, 0);
        form.add(cbPaciente, 1, 0);
        form.add(lblMedico, 0, 1);
        form.add(cbMedico, 1, 1);
        form.add(lblData, 0, 2);
        form.add(dpData, 1, 2);
        form.add(lblHora, 0, 3);
        form.add(cbHora, 1, 3);

        HBox botoes = new HBox(10, btnAgendar, btnCancelar);

        Label lblLista = new Label("Consultas agendadas");
        lblLista.getStyleClass().add("titulo-lista");

        VBox root = new VBox(16, titulo, form, botoes, lblLista, listaAgendamentos);
        root.setPadding(new Insets(24));
        return root;
    }

    /**
     * Recarrega as listas de pacientes e médicos nos ComboBox.
     * Chamado pela MainApp sempre que o usuário clica na aba de
     * Agendamentos, garantindo que cadastros novos apareçam aqui.
     */
    public void atualizarCombos() {
        if (cbPaciente != null) {
            Paciente selecionadoPaciente = cbPaciente.getValue();
            cbPaciente.getItems().setAll(pacienteDAO.listarTodos());
            cbPaciente.setValue(selecionadoPaciente);
        }
        if (cbMedico != null) {
            Medico selecionadoMedico = cbMedico.getValue();
            cbMedico.getItems().setAll(medicoDAO.listarTodos());
            cbMedico.setValue(selecionadoMedico);
        }
    }

    private void agendarConsulta() {
        try {
            if (cbPaciente.getValue() == null || cbMedico.getValue() == null
                    || dpData.getValue() == null || cbHora.getValue() == null) {
                mostrarAlerta("Preencha todos os campos antes de agendar.");
                return;
            }

            LocalTime hora = LocalTime.parse(cbHora.getValue());

            Agendamento agendamento = new Agendamento(
                    cbPaciente.getValue(),
                    cbMedico.getValue(),
                    dpData.getValue(),
                    hora
            );

            // O DAO verifica conflito internamente e lança
            // IllegalStateException se o médico já tiver consulta
            // nesse horário. Aqui só tratamos a mensagem para o usuário.
            agendamentoDAO.salvar(agendamento);

            atualizarLista();
            mostrarInfo("Consulta agendada com sucesso!");

        } catch (IllegalStateException conflito) {
            // Esta é a regra de negócio "impedir agendamento duplo"
            // sendo respeitada e comunicada ao usuário na tela.
            mostrarAlerta(conflito.getMessage());

        } catch (Exception ex) {
            mostrarAlerta("Erro ao agendar consulta: " + ex.getMessage());
        }
    }

    private void cancelarSelecionada() {
        Agendamento selecionado = listaAgendamentos.getSelectionModel().getSelectedItem();
        if (selecionado == null) {
            mostrarAlerta("Selecione uma consulta na lista para cancelar.");
            return;
        }

        agendamentoDAO.excluir(selecionado.getId());
        atualizarLista();
    }

    private void atualizarLista() {
        List<Agendamento> agendamentos = agendamentoDAO.listarTodos();
        listaAgendamentos.getItems().setAll(agendamentos);
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
