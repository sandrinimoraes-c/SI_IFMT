-- ============================================================
-- Sistema de Animais de Rua e Adoção — Pontes e Lacerda (MT)
-- Script de criação do banco de dados (MySQL 8 / MariaDB 10.5+)
-- ============================================================

CREATE DATABASE IF NOT EXISTS animais_pontes_lacerda
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE animais_pontes_lacerda;

-- ------------------------------------------------------------
-- Usuários do sistema (voluntários e administradores)
-- A senha é guardada como hash (nunca em texto puro).
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome        VARCHAR(120) NOT NULL,
    login       VARCHAR(50)  NOT NULL,
    senha_hash  VARCHAR(255) NOT NULL,
    perfil      ENUM('admin', 'voluntario') NOT NULL DEFAULT 'voluntario',
    ativo       BOOLEAN      NOT NULL DEFAULT TRUE,
    criado_em   TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_usuarios_login (login)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Animais acolhidos pelo abrigo / protetores
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS animais (
    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome                VARCHAR(80)  NULL,
    especie             ENUM('cachorro', 'gato', 'outro') NOT NULL,
    raca                VARCHAR(80)  NULL,
    sexo                ENUM('macho', 'femea', 'indefinido') NOT NULL DEFAULT 'indefinido',
    porte               ENUM('pequeno', 'medio', 'grande') NULL,
    cor                 VARCHAR(60)  NULL,
    idade_meses         SMALLINT UNSIGNED NULL,          -- idade aproximada
    status              ENUM('em_tratamento', 'abrigado', 'disponivel_adocao', 'adotado', 'falecido')
                        NOT NULL DEFAULT 'abrigado',
    observacoes         TEXT         NULL,
    data_cadastro       DATE         NOT NULL DEFAULT (CURRENT_DATE),
    usuario_id          INT UNSIGNED NOT NULL,           -- quem cadastrou
    PRIMARY KEY (id),
    KEY idx_animais_status (status),
    CONSTRAINT fk_animais_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Resgates / ocorrências: animal visto na rua.
-- animal_id fica NULL até o animal ser resgatado e cadastrado.
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS resgates (
    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    animal_id           INT UNSIGNED NULL,
    data_ocorrencia     DATE         NOT NULL,
    bairro              VARCHAR(80)  NOT NULL,
    local_referencia    VARCHAR(200) NULL,
    descricao           TEXT         NULL,
    situacao            ENUM('aberta', 'em_andamento', 'resgatado', 'encerrada')
                        NOT NULL DEFAULT 'aberta',
    informante_nome     VARCHAR(120) NULL,
    informante_telefone VARCHAR(20)  NULL,
    usuario_id          INT UNSIGNED NOT NULL,           -- quem registrou
    PRIMARY KEY (id),
    KEY idx_resgates_situacao (situacao),
    CONSTRAINT fk_resgates_animal
        FOREIGN KEY (animal_id) REFERENCES animais (id)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_resgates_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Atendimentos de saúde: vacinas, castração, consultas etc.
-- proxima_dose alimenta o relatório de vacinas pendentes.
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS atendimentos_saude (
    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    animal_id           INT UNSIGNED NOT NULL,
    tipo                ENUM('vacina', 'castracao', 'vermifugo', 'consulta', 'cirurgia', 'outro') NOT NULL,
    descricao           VARCHAR(255) NULL,
    data_atendimento    DATE         NOT NULL,
    proxima_dose        DATE         NULL,
    veterinario         VARCHAR(120) NULL,
    PRIMARY KEY (id),
    KEY idx_atendimentos_proxima (proxima_dose),
    CONSTRAINT fk_atendimentos_animal
        FOREIGN KEY (animal_id) REFERENCES animais (id)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Adotantes (pessoas interessadas em adotar)
-- Contém dados pessoais: tratar conforme a LGPD.
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS adotantes (
    id                      INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome                    VARCHAR(120) NOT NULL,
    cpf                     CHAR(11)     NOT NULL,
    telefone                VARCHAR(20)  NOT NULL,
    email                   VARCHAR(120) NULL,
    endereco                VARCHAR(200) NULL,
    bairro                  VARCHAR(80)  NULL,
    cidade                  VARCHAR(80)  NOT NULL DEFAULT 'Pontes e Lacerda',
    tipo_moradia            ENUM('casa', 'apartamento', 'sitio_chacara', 'outro') NULL,
    possui_outros_animais   BOOLEAN      NOT NULL DEFAULT FALSE,
    observacoes             TEXT         NULL,
    data_cadastro           DATE         NOT NULL DEFAULT (CURRENT_DATE),
    PRIMARY KEY (id),
    UNIQUE KEY uk_adotantes_cpf (cpf)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- Adoções: liga animal e adotante. Tabela separada para manter
-- o histórico quando um animal é devolvido e readotado.
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS adocoes (
    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    animal_id           INT UNSIGNED NOT NULL,
    adotante_id         INT UNSIGNED NOT NULL,
    data_adocao         DATE         NOT NULL,
    situacao            ENUM('ativa', 'devolvida') NOT NULL DEFAULT 'ativa',
    data_devolucao      DATE         NULL,
    observacoes         TEXT         NULL,
    usuario_id          INT UNSIGNED NOT NULL,           -- quem registrou
    PRIMARY KEY (id),
    KEY idx_adocoes_animal (animal_id),
    KEY idx_adocoes_adotante (adotante_id),
    CONSTRAINT fk_adocoes_animal
        FOREIGN KEY (animal_id) REFERENCES animais (id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_adocoes_adotante
        FOREIGN KEY (adotante_id) REFERENCES adotantes (id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_adocoes_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;
