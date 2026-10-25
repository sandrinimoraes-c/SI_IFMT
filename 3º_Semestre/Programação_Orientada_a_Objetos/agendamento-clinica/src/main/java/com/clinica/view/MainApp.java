package com.clinica.view;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.stage.Stage;

/**
 * Tela principal do sistema.
 *
 * Esta classe NÃO contém nenhuma linha de SQL — apenas monta um
 * TabPane com 3 abas (Pacientes, Médicos, Agendamentos) e coloca o
 * conteúdo de cada View dentro da aba correspondente.
 *
 * Cada View continua 100% responsável pelo seu próprio formulário e
 * pela comunicação com seu DAO; a MainApp só organiza a navegação.
 */
public class MainApp extends Application {

    @Override
    public void start(Stage primaryStage) {

        CadastroPacienteView pacienteView = new CadastroPacienteView();
        CadastroMedicoView medicoView = new CadastroMedicoView();
        AgendamentoView agendamentoView = new AgendamentoView();

        Tab tabPacientes = new Tab("Pacientes", pacienteView.getContent());
        Tab tabMedicos = new Tab("Médicos", medicoView.getContent());
        Tab tabAgendamentos = new Tab("Agendamentos", agendamentoView.getContent());

        // As abas não podem ser fechadas pelo usuário (sem o "x").
        tabPacientes.setClosable(false);
        tabMedicos.setClosable(false);
        tabAgendamentos.setClosable(false);

        TabPane tabPane = new TabPane(tabPacientes, tabMedicos, tabAgendamentos);

        // Sempre que o usuário entra na aba de Agendamentos, recarrega
        // os ComboBox de Paciente/Médico, para já trazer cadastros
        // novos feitos nas outras abas.
        tabPane.getSelectionModel().selectedItemProperty().addListener((obs, antiga, nova) -> {
            if (nova == tabAgendamentos) {
                agendamentoView.atualizarCombos();
            }
        });

        Scene scene = new Scene(tabPane, 720, 640);
        scene.getStylesheets().add(getClass().getResource("/styles.css").toExternalForm());

        primaryStage.getIcons().add(
                new javafx.scene.image.Image(getClass().getResourceAsStream("/icone.png"))
        );
        primaryStage.setTitle("Plataforma de Agendamento de Consultas Médicas");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
