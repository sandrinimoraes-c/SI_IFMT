package com.clinica.dao.impl;

import com.clinica.dao.MedicoDAO;
import com.clinica.factory.ConexaoFactory;
import com.clinica.model.Medico;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Implementação concreta de MedicoDAO. Mesmo padrão de PacienteDAOImpl:
 * todo o SQL relativo a Médico fica isolado aqui.
 */
public class MedicoDAOImpl implements MedicoDAO {

    @Override
    public void salvar(Medico medico) {
        String sql = "INSERT INTO medico (nome, crm, especialidade) VALUES (?, ?, ?)";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, medico.getNome());
            stmt.setString(2, medico.getCrm());
            stmt.setString(3, medico.getEspecialidade());

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao salvar médico: " + e.getMessage(), e);
        }
    }

    @Override
    public void atualizar(Medico medico) {
        String sql = "UPDATE medico SET nome = ?, crm = ?, especialidade = ? WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, medico.getNome());
            stmt.setString(2, medico.getCrm());
            stmt.setString(3, medico.getEspecialidade());
            stmt.setInt(4, medico.getId());

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao atualizar médico: " + e.getMessage(), e);
        }
    }

    @Override
    public void excluir(int id) {
        String sql = "DELETE FROM medico WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao excluir médico: " + e.getMessage(), e);
        }
    }

    @Override
    public Medico buscarPorId(int id) {
        String sql = "SELECT * FROM medico WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                return mapearMedico(rs);
            }
            return null;

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao buscar médico: " + e.getMessage(), e);
        }
    }

    @Override
    public List<Medico> listarTodos() {
        String sql = "SELECT * FROM medico ORDER BY nome";
        List<Medico> medicos = new ArrayList<>();

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                medicos.add(mapearMedico(rs));
            }

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao listar médicos: " + e.getMessage(), e);
        }

        return medicos;
    }

    private Medico mapearMedico(ResultSet rs) throws SQLException {
        Medico m = new Medico();
        m.setId(rs.getInt("id"));
        m.setNome(rs.getString("nome"));
        m.setCrm(rs.getString("crm"));
        m.setEspecialidade(rs.getString("especialidade"));
        return m;
    }
}
