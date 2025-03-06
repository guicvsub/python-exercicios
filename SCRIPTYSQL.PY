/*
-) Crie a tabela INSTRUTOR (a partir da estrutura mostrada na tabela 1), já inserindo 
durante a criação, as constraints necessárias. O nome do instrutor não pode estar 
vazio.
Obs: os campos em negrito representam uma chave primária
CREATE TABLE INTRUTOR(
 IDINST NUMBER(3) PRIMARY KEY, 
 NOME VARCHAR2(40) NOT NULL,
TELEFONE VARCHAR2(11),
SALARIO FLOAT(10),
DT VARCHAR2(3) 
);
*/

/*Apague do banco de dados a constraint de chave primária da tabela INSTRUTOR, 
inserindo-a novamente.*/
//ALTER TABLE INTRUTOR DROP PRIMARY KEY,

//ALTER TABLE INTRUTOR MODIFY IDINST PRIMARY KEY


/*3-) Crie a tabela TURMA definindo as colunas e suas restrições de chaves. Ocorreu 
algum erro? Porque ocorreu este erro? Faça o exercício 5 e retorne para este 
exercício criando a tabela, inclusive com a chave primária.*/
// DEU PAU SEM REFERENCIA SO FAZER A PRICIPAIS PRIMEIRO  

/*Crie a tabela TURMA definindo as colunas e suas restrições de chaves. Ocorreu 
algum erro? Porque ocorreu este erro? Faça o exercício 5 e retorne para este 
exercício criando a tabela, inclusive com a chave primária.*/

//4-) Crie a tabela ALUNO com todas as constraints.
CREATE TABLE ALUNO (
MATRIC NUMBER(6) PRIMARY KEY 




);

CREATE TABLE CURSO(
IDCURSO NUMBER(3) PRIMARY KEY, 
NOME VARCHAR(40) NOT NULL,
CARGAR_HORARIA VARCHAR2(4),
PRECO VARCHAR2(4),
PRE_REQUISITO VARCHAR(40)


);


