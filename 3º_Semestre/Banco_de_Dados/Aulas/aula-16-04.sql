create table Alunos (
	idAluno integer,
	nome varchar (45),
	curso char (45),
    semestre integer,
    primary key (idAluno) );
                    
insert into Alunos (idAluno, nome, curso, semestre)
values (1002, 'Maria', 'Sistemas de Informação', 2);

insert into Alunos (idAluno, nome, curso, semestre)
values (1030, 'Fernanda', 'Sistemas de Informação', 4);

delete
from Alunos as A
where A.idAluno = 1030;

delete 
from Alunos as A
where A.nome = 'Fernanda'; 

delete
from Alunos as A
where A.idAluno = 1002;

create table Monitoria (
	disciplina char (15),
    idAluno integer,
    orientador char (30),
    PRIMARY KEY (disciplina, idAluno),
    FOREIGN KEY (idAluno) REFERENCES Alunos (idAluno)
    on delete cascade);
    
drop table monitoria;
drop table Alunos;

insert into Monitoria (disciplina, idAluno, orientador)
values ('Programação', 1002, 'Carlos');

insert into Monitoria (disciplina, idAluno, orientador)
values ('Programação', 1030, 'Carlos');

insert into Monitoria (disciplina, idAluno, orientador)
values ('Programação', 1040, 'Carlos');

update Alunos
set curso = 'Ciências biológicas'
where idAluno = 1030;

select * from Alunos;
select * from Monitoria;
