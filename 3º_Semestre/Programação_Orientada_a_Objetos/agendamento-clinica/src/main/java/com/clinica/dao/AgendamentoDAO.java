package com.clinica.dao;

import com.clinica.model.Agendamento;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

/**
 * Interface DAO para Agendamento.
 *
 * Note o método existeConflito(): ele representa a regra de negócio
 * "o sistema deve impedir o agendamento de duas consultas para o
 * mesmo médico no mesmo horário", exigida no edital. A verificação
 * em si (o SELECT) fica na implementação; aqui só declaramos o contrato.
 */
public interface AgendamentoDAO {

    void salvar(Agendamento agendamento);

    void atualizar(Agendamento agendamento);

    void excluir(int id);

    Agendamento buscarPorId(int id);

    List<Agendamento> listarTodos();

    /**
     * Verifica se já existe uma consulta marcada para o médico
     * informado, na mesma data e hora.
     *
     * @return true se já existir conflito de horário, false se o
     *         horário estiver livre para aquele médico.
     */
    boolean existeConflito(int medicoId, LocalDate data, LocalTime hora);
}
