package com.clinica.factory;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Factory responsável por criar e fornecer conexões com o banco MySQL.
 *
 * Este é o Padrão Factory exigido no edital: centraliza em UM único
 * lugar a lógica de "como conectar no banco". Nenhuma outra classe
 * do sistema sabe a URL, usuário ou senha do banco — todas pedem
 * a conexão para esta fábrica.
 *
 * Se um dia o banco mudar de servidor, ou de MySQL para outro SGBD,
 * só este arquivo precisa ser alterado.
 */
public class ConexaoFactory {

    private static final String URL = "jdbc:mysql://localhost:3306/clinica_db?useTimezone=true&serverTimezone=UTC";
    private static final String USUARIO = "root";
    private static final String SENHA = "10111997"; // troque pela senha do seu MySQL

    /**
     * Cria e retorna uma nova conexão com o banco de dados.
     * Cada chamada gera uma conexão nova (abordagem simples,
     * suficiente para um projeto acadêmico).
     */
    public static Connection criarConexao() {
        try {
            return DriverManager.getConnection(URL, USUARIO, SENHA);
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao conectar ao banco de dados: " + e.getMessage(), e);
        }
    }
}
