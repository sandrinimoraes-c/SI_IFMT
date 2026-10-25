package com.clinica.dao;

import com.clinica.model.Medico;
import java.util.List;

/**
 * Interface DAO para Médico. Mesmo conceito de PacienteDAO:
 * define o contrato, sem detalhes de implementação/SQL.
 */
public interface MedicoDAO {

    void salvar(Medico medico);

    void atualizar(Medico medico);

    void excluir(int id);

    Medico buscarPorId(int id);

    List<Medico> listarTodos();
}
