package com.clinica.model;

import java.time.LocalDate;
import java.time.LocalTime;

/**
 * Classe de modelo (entidade) que representa um Agendamento.
 *
 * Note que aqui guardamos os OBJETOS Paciente e Medico completos,
 * não apenas os IDs. Isso facilita exibir os dados na tela
 * (ex.: tabela de agendamentos) sem precisar fazer outra consulta
 * ao banco só para mostrar o nome do paciente/médico.
 */
public class Agendamento {

    private int id;
    private Paciente paciente;
    private Medico medico;
    private LocalDate dataConsulta;
    private LocalTime horaConsulta;
    private String status; // ex.: "AGENDADA", "CANCELADA", "REALIZADA"

    public Agendamento() {
    }

    public Agendamento(Paciente paciente, Medico medico, LocalDate dataConsulta, LocalTime horaConsulta) {
        this.paciente = paciente;
        this.medico = medico;
        this.dataConsulta = dataConsulta;
        this.horaConsulta = horaConsulta;
        this.status = "AGENDADA";
    }

    public Agendamento(int id, Paciente paciente, Medico medico, LocalDate dataConsulta,
                        LocalTime horaConsulta, String status) {
        this.id = id;
        this.paciente = paciente;
        this.medico = medico;
        this.dataConsulta = dataConsulta;
        this.horaConsulta = horaConsulta;
        this.status = status;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

    public Medico getMedico() {
        return medico;
    }

    public void setMedico(Medico medico) {
        this.medico = medico;
    }

    public LocalDate getDataConsulta() {
        return dataConsulta;
    }

    public void setDataConsulta(LocalDate dataConsulta) {
        this.dataConsulta = dataConsulta;
    }

    public LocalTime getHoraConsulta() {
        return horaConsulta;
    }

    public void setHoraConsulta(LocalTime horaConsulta) {
        this.horaConsulta = horaConsulta;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Consulta de " + paciente.getNome() + " com " + medico.getNome()
                + " em " + dataConsulta + " às " + horaConsulta;
    }
}
