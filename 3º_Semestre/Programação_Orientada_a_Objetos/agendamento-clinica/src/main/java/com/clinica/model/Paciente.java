package com.clinica.model;

import java.time.LocalDate;

/**
 * Classe de modelo (entidade) que representa um Paciente.
 *
 * Esta classe é "burra" de propósito: não conhece banco de dados,
 * não conhece tela. Apenas guarda dados e expõe getters/setters.
 * Isso é o que o edital chama de "modelo" na arquitetura em camadas.
 */
public class Paciente {

    private int id;
    private String nome;
    private String cpf;
    private String telefone;
    private LocalDate dataNascimento;

    public Paciente() {
    }

    public Paciente(String nome, String cpf, String telefone, LocalDate dataNascimento) {
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.dataNascimento = dataNascimento;
    }

    public Paciente(int id, String nome, String cpf, String telefone, LocalDate dataNascimento) {
        this.id = id;
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.dataNascimento = dataNascimento;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public LocalDate getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    /**
     * Usado pela ComboBox/ListView do JavaFX para exibir o paciente
     * de forma legível (em vez de "com.clinica.model.Paciente@1b2c3d").
     */
    @Override
    public String toString() {
        return nome + " (CPF: " + cpf + ")";
    }
}
