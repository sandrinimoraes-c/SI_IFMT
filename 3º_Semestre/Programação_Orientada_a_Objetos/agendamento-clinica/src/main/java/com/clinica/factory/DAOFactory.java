package com.clinica.factory;

import com.clinica.dao.AgendamentoDAO;
import com.clinica.dao.MedicoDAO;
import com.clinica.dao.PacienteDAO;
import com.clinica.dao.impl.AgendamentoDAOImpl;
import com.clinica.dao.impl.MedicoDAOImpl;
import com.clinica.dao.impl.PacienteDAOImpl;

/**
 * Factory responsável por entregar a implementação correta de cada DAO.
 *
 * Esta é a peça-chave do "Padrão de Projeto DAO e Factory com
 * polimorfismo" pedido no edital: as telas (view) pedem o DAO
 * para esta fábrica e recebem de volta um objeto do TIPO da
 * interface (PacienteDAO), mas que por trás é uma implementação
 * concreta (PacienteDAOImpl). Isso é polimorfismo na prática.
 *
 * Exemplo de uso em qualquer tela:
 *     PacienteDAO dao = DAOFactory.getPacienteDAO();
 *     dao.salvar(paciente);
 *
 * A tela nunca usa "new PacienteDAOImpl()" diretamente — sempre
 * passa pela fábrica.
 */
public class DAOFactory {

    public static PacienteDAO getPacienteDAO() {
        return new PacienteDAOImpl();
    }

    public static MedicoDAO getMedicoDAO() {
        return new MedicoDAOImpl();
    }

    public static AgendamentoDAO getAgendamentoDAO() {
        return new AgendamentoDAOImpl();
    }
}
