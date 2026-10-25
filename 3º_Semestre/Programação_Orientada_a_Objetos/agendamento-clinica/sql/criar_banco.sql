
CREATE DATABASE IF NOT EXISTS clinica_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE clinica_db;

SELECT * FROM paciente;
SELECT * FROM medico;
SELECT * FROM agendamento;

CREATE TABLE IF NOT EXISTS paciente (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(120) NOT NULL,
    cpf         VARCHAR(14)  NOT NULL UNIQUE,
    telefone    VARCHAR(20),
    data_nascimento DATE
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS medico (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    nome         VARCHAR(120) NOT NULL,
    crm          VARCHAR(20)  NOT NULL UNIQUE,
    especialidade VARCHAR(80) NOT NULL
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS agendamento (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id   INT NOT NULL,
    medico_id     INT NOT NULL,
    data_consulta DATE NOT NULL,
    hora_consulta TIME NOT NULL,
    status        VARCHAR(20) NOT NULL DEFAULT 'AGENDADA',
    CONSTRAINT fk_agendamento_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id) ON DELETE CASCADE,
    CONSTRAINT fk_agendamento_medico FOREIGN KEY (medico_id) REFERENCES medico(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Observação: a regra de negócio "não permitir dois agendamentos para o
-- mesmo médico no mesmo horário" é validada em Java, dentro do
-- AgendamentoDAOImpl, antes do INSERT (ver método existeConflito()).
-- Isso é proposital: mantém a regra de negócio na camada de
-- persistência/Java, e não "escondida" só no banco.

INSERT INTO medico (nome, crm, especialidade) VALUES
    ('Dra. Ana Souza', 'CRM-MT 1234', 'Cardiologia'),
    ('Dr. Carlos Lima', 'CRM-MT 5678', 'Pediatria');

INSERT INTO paciente (nome, cpf, telefone, data_nascimento) VALUES
    ('João da Silva', '123.456.789-00', '(65) 99999-0001', '1990-05-10'),
    ('Maria Oliveira', '987.654.321-00', '(65) 99999-0002', '1985-11-22');
