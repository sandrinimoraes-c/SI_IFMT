package com.clinica.dao.impl;

import com.clinica.dao.PacienteDAO;
import com.clinica.factory.ConexaoFactory;
import com.clinica.model.Paciente;

import java.sql.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Implementação concreta de PacienteDAO.
 *
 * TODO o SQL do sistema relacionado a Paciente fica AQUI, e somente
 * aqui. Isso atende ao requisito "Encapsulamento de Infraestrutura":
 * nenhuma classe de tela (view) contém SELECT/INSERT/UPDATE/DELETE.
 *
 * Sempre usamos PreparedStatement (nunca concatenação de String)
 * para evitar SQL Injection.
 */
public class PacienteDAOImpl implements PacienteDAO {

    @Override
    public void salvar(Paciente paciente) {
        String sql = "INSERT INTO paciente (nome, cpf, telefone, data_nascimento) VALUES (?, ?, ?, ?)";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, paciente.getNome());
            stmt.setString(2, paciente.getCpf());
            stmt.setString(3, paciente.getTelefone());
            stmt.setDate(4, Date.valueOf(paciente.getDataNascimento()));

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao salvar paciente: " + e.getMessage(), e);
        }
    }

    @Override
    public void atualizar(Paciente paciente) {
        String sql = "UPDATE paciente SET nome = ?, cpf = ?, telefone = ?, data_nascimento = ? WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, paciente.getNome());
            stmt.setString(2, paciente.getCpf());
            stmt.setString(3, paciente.getTelefone());
            stmt.setDate(4, Date.valueOf(paciente.getDataNascimento()));
            stmt.setInt(5, paciente.getId());

            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao atualizar paciente: " + e.getMessage(), e);
        }
    }

    @Override
    public void excluir(int id) {
        String sql = "DELETE FROM paciente WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            stmt.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao excluir paciente: " + e.getMessage(), e);
        }
    }

    @Override
    public Paciente buscarPorId(int id) {
        String sql = "SELECT * FROM paciente WHERE id = ?";

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                return mapearPaciente(rs);
            }
            return null;

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao buscar paciente: " + e.getMessage(), e);
        }
    }

    @Override
    public List<Paciente> listarTodos() {
        String sql = "SELECT * FROM paciente ORDER BY nome";
        List<Paciente> pacientes = new ArrayList<>();

        try (Connection conn = ConexaoFactory.criarConexao();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                pacientes.add(mapearPaciente(rs));
            }

        } catch (SQLException e) {
            throw new RuntimeException("Erro ao listar pacientes: " + e.getMessage(), e);
        }

        return pacientes;
    }

    /**
     * Método auxiliar privado: converte uma linha do ResultSet
     * em um objeto Paciente. Evita repetir esse código em
     * buscarPorId() e listarTodos().
     */
    private Paciente mapearPaciente(ResultSet rs) throws SQLException {
        Paciente p = new Paciente();
        p.setId(rs.getInt("id"));
        p.setNome(rs.getString("nome"));
        p.setCpf(rs.getString("cpf"));
        p.setTelefone(rs.getString("telefone"));

        Date data = rs.getDate("data_nascimento");
        if (data != null) {
            p.setDataNascimento(data.toLocalDate());
        }

        return p;
    }
}
