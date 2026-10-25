package com.clinica.model;

/**
 * Classe de modelo (entidade) que representa um Médico.
 * Assim como Paciente, não tem nenhuma lógica de banco ou tela.
 */
public class Medico {

    private int id;
    private String nome;
    private String crm;
    private String especialidade;

    public Medico() {
    }

    public Medico(String nome, String crm, String especialidade) {
        this.nome = nome;
        this.crm = crm;
        this.especialidade = especialidade;
    }

    public Medico(int id, String nome, String crm, String especialidade) {
        this.id = id;
        this.nome = nome;
        this.crm = crm;
        this.especialidade = especialidade;
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

    public String getCrm() {
        return crm;
    }

    public void setCrm(String crm) {
        this.crm = crm;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    @Override
    public String toString() {
        return nome + " - " + especialidade;
    }
}
