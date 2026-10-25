package com.clinica.dao;

import com.clinica.model.Paciente;
import java.util.List;

/**
 * Interface DAO (Data Access Object) para Paciente.
 *
 * Esta interface é o "contrato": define O QUE pode ser feito
 * com um Paciente no banco, mas não COMO. O "como" (o SQL)
 * fica escondido dentro de PacienteDAOImpl.
 *
 * Vantagem: a tela (view) e qualquer outra classe do sistema
 * só conhecem esta interface. Se um dia trocarmos MySQL por
 * outro banco, criamos uma nova implementação (ex.: PacienteDAOPostgres)
 * e nada na tela precisa mudar.
 */
public interface PacienteDAO {

    void salvar(Paciente paciente);

    void atualizar(Paciente paciente);

    void excluir(int id);

    Paciente buscarPorId(int id);

    List<Paciente> listarTodos();
}
