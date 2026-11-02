# Diagrama Entidade-Relacionamento

Banco: `animais_pontes_lacerda` (script em [`banco/schema.sql`](../banco/schema.sql)).

```mermaid
erDiagram
    USUARIOS ||--o{ ANIMAIS : cadastra
    USUARIOS ||--o{ RESGATES : registra
    USUARIOS ||--o{ ADOCOES : registra
    ANIMAIS ||--o{ ATENDIMENTOS_SAUDE : recebe
    ANIMAIS ||--o{ ADOCOES : "e adotado em"
    ANIMAIS |o--o{ RESGATES : "origina"
    ADOTANTES ||--o{ ADOCOES : realiza

    USUARIOS {
        int id PK
        string nome
        string login UK
        string senha_hash
        string perfil
        boolean ativo
        timestamp criado_em
    }

    ANIMAIS {
        int id PK
        string nome
        string especie
        string raca
        string sexo
        string porte
        string cor
        int idade_meses
        string status
        text observacoes
        date data_cadastro
        int usuario_id FK
    }

    RESGATES {
        int id PK
        int animal_id FK
        date data_ocorrencia
        string bairro
        string local_referencia
        text descricao
        string situacao
        string informante_nome
        string informante_telefone
        int usuario_id FK
    }

    ATENDIMENTOS_SAUDE {
        int id PK
        int animal_id FK
        string tipo
        string descricao
        date data_atendimento
        date proxima_dose
        string veterinario
    }

    ADOTANTES {
        int id PK
        string nome
        string cpf UK
        string telefone
        string email
        string endereco
        string bairro
        string cidade
        string tipo_moradia
        boolean possui_outros_animais
        text observacoes
        date data_cadastro
    }

    ADOCOES {
        int id PK
        int animal_id FK
        int adotante_id FK
        date data_adocao
        string situacao
        date data_devolucao
        text observacoes
        int usuario_id FK
    }
```

## Relacionamentos

| Relação | Cardinalidade | Explicação |
|---------|---------------|------------|
| usuarios → animais | 1:N | cada animal é cadastrado por um usuário |
| usuarios → resgates | 1:N | cada ocorrência é registrada por um usuário |
| usuarios → adocoes | 1:N | cada adoção é registrada por um usuário |
| animais → atendimentos_saude | 1:N | um animal tem vários atendimentos (vacinas, castração...) |
| animais → resgates | 1:N (opcional) | a ocorrência só aponta para um animal depois do resgate |
| animais → adocoes | 1:N | um animal pode ser adotado, devolvido e readotado |
| adotantes → adocoes | 1:N | um adotante pode adotar mais de um animal |

`adocoes` é a tabela associativa entre `animais` e `adotantes` (relação N:N com atributos próprios: data, situação e devolução).
