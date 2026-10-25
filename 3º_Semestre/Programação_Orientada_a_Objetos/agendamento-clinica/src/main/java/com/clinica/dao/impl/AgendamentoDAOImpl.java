package com.clinica.dao.impl;

import com.clinica.dao.AgendamentoDAO;
import com.clinica.dao.MedicoDAO;
import com.clinica.dao.PacienteDAO;
import com.clinica.factory.ConexaoFactory;
import com.clinica.factory.DAOFactory;
import com.clinica.model.Agendamento;
import com.clinica.model.Medico;
import com.clinica.model.Paciente;

import java.sql.*;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

/**
 * Implementação concreta de AgendamentoDAO.
 *
 * Ponto-chave do projeto: o método salvar() chama existeConflito()
 * ANTES de inserir no banco. Se já existir uma consulta para o
 * mesmo médico na mesma data/hora, lançamos uma exceção e a tela
 * mostra um alerta ao usuário — o INSERT nunca chega a ser executado.
 */
public class AgendamentoDAOImpl implements AgendamentoDAO {

    @Override
    public void salvar(Agendamento agendamento) {

        // Regra de negócio: impedir duas consultas para o mesmo
        // médico no mesmo horário.
        boolean conflito = existeConflito(
                agendamento.getMedico().getId(),
                agendamento.getDataConsulta(),
                agendamento.getHoraConsulta()
        );

        if (conflito) {
            throw new IllegalStateException(
                    "Este médico já possui uma consulta agendada nesta data e horário."
            );
        }

        String sql = "INSERT INTO agendamento (paciente_id, medico_id, data_consulta, hora_consulta, status) "
                + "VALUES (?, ?, ?, ?, ?)";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, agendamento.getPaciente().getId());
            stmt.setInt(2, agendamento.getMedico().getId());
            stmt.setDate(3, Date.valueOf(agendamento.getDataConsulta()));
            stmt.setTime(4, Time.valueOf(agendamento.getHoraConsulta()));
            stmt.setString(5, agendamento.getStatus());

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao salvar agendamento: " + e.getMessage(), e);
        }
    }

    @Override
    public void atualizar(Agendamento agendamento) {
        String sql = "UPDATE agendamento SET paciente_id = ?, medico_id = ?, data_consulta = ?, "
                + "hora_consulta = ?, status = ? WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, agendamento.getPaciente().getId());
            stmt.setInt(2, agendamento.getMedico().getId());
            stmt.setDate(3, Date.valueOf(agendamento.getDataConsulta()));
            stmt.setTime(4, Time.valueOf(agendamento.getHoraConsulta()));
            stmt.setString(5, agendamento.getStatus());
            stmt.setInt(6, agendamento.getId());

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao atualizar agendamento: " + e.getMessage(), e);
        }
    }

    @Override
    public void excluir(int id) {
        String sql = "DELETE FROM agendamento WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao excluir agendamento: " + e.getMessage(), e);
        }
    }

    @Override
    public Agendamento buscarPorId(int id) {
        String sql = "SELECT * FROM agendamento WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                return mapearAgendamento(rs);
            }
            return null;

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao buscar agendamento: " + e.getMessage(), e);
        }
    }

    @Override
    public List<Agendamento> listarTodos() {
        String sql = "SELECT * FROM agendamento ORDER BY data_consulta, hora_consulta";
        List<Agendamento> agendamentos = new ArrayList<>();

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                agendamentos.add(mapearAgendamento(rs));
            }

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao listar agendamentos: " + e.getMessage(), e);
        }

        return agendamentos;
    }

    @Override
    public boolean existeConflito(int medicoId, LocalDate data, LocalTime hora) {
        String sql = "SELECT COUNT(*) FROM agendamento "
                + "WHERE medico_id = ? AND data_consulta = ? AND hora_consulta = ? "
                + "AND status <> 'CANCELADA'";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, medicoId);
            stmt.setDate(2, Date.valueOf(data));
            stmt.setTime(3, Time.valueOf(hora));

            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return rs.getInt(1) > 0;
            }
            return false;

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao verificar conflito de agendamento: " + e.getMessage(), e);
        }
    }

    /**
     * Converte uma linha do ResultSet em um objeto Agendamento completo,
     * já carregando o Paciente e o Médico associados (usando os outros
     * DAOs, via DAOFactory).
     */
    private Agendamento mapearAgendamento(ResultSet rs) throws SQLException {
        PacienteDAO pacienteDAO = DAOFactory.getPacienteDAO();
        MedicoDAO medicoDAO = DAOFactory.getMedicoDAO();

        Paciente paciente = pacienteDAO.buscarPorId(rs.getInt("paciente_id"));
        Medico medico = medicoDAO.buscarPorId(rs.getInt("medico_id"));

        Agendamento agendamento = new Agendamento();
        agendamento.setId(rs.getInt("id"));
        agendamento.setPaciente(paciente);
        agendamento.setMedico(medico);
        agendamento.setDataConsulta(rs.getDate("data_consulta").toLocalDate());
        agendamento.setHoraConsulta(rs.getTime("hora_consulta").toLocalTime());
        agendamento.setStatus(rs.getString("status"));

        return agendamento;
    }
}
