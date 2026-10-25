create table Alunos (
	idAluno integer,
	nome varchar (45),
	curso char (45),
    semestre integer,
    primary key (idAluno) );
                    
insert into Alunos (idAluno, nome, curso, semestre)
values (1002, 'Maria', 'Administração', 2);

insert into Alunos (idAluno, nome, curso, semestre)
values (1003, 'Fernanda', 'Sistemas de Informação', 4);

create table Monitoria (
	disciplina char (15),
    idAluno integer,
    orientador char (30),
    PRIMARY KEY (disciplina, idAluno),
    FOREIGN KEY (idAluno) REFERENCES Alunos (idAluno));

insert into Monitoria (disciplina, idAluno, orientador)
values ('Programação', 1002, 'Jorge');

insert into Monitoria (disciplina, idAluno, orientador)
values ('Programação', 1003, 'Carlos');