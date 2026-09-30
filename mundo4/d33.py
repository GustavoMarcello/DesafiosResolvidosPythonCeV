"""
# Video com os desafios:  CeV Python POO: Aula 12 https://www.youtube.com/watch?v=CTbdydT9nlQ&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=27

EXERCÍCIO D32 - Pessoa
Crie um programa que:
1. Contenha a classe abstrata Pessoa contendo:
    - _nome
    - _ano_nascimento (validar se a data é válida entre 01/01/1900 e a data atual)
    - @nascimento
    - @idade (não pode ser alterada pelo usuário)
2. Crie a classe filha Aluno contendo:
    - cursosOferecidos = ['ADM', 'TI', 'RH', 'Marketing', 'ADS']
    - addCursoOferecidos(curso) - adiciona um curso à lista de cursos oferecidos
    - _curso
"""
from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome:str, ano_nascimento:str):
        self._nome = nome
        self.verificaIdade(ano_nascimento)
        self._ano_nascimento = ano_nascimento


    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        raise PermissionError(f'idade não pode ser alterada')

    @property
    def ano_nascimento(self):
        return self._ano_nascimento

    @ano_nascimento.setter
    def ano_nascimento(self, ano_nascimento):
        self.verificaIdade(ano_nascimento)
        self._ano_nascimento = ano_nascimento
        print('Ano nascimento alterado com sucesso')


    def verificaIdade(self, ano_nascimento):
        ano_atual = datetime.now().year
        if ano_nascimento >= ano_atual or ano_nascimento < 1900:
            raise AttributeError(f'Idade inválida, insira valores entre 1900 até ano atual')
        
        self._idade = ano_atual - ano_nascimento

class Aluno(Pessoa):
    def __init__(self, nome:str, ano_nascimento:str, curso:str):
        super().__init__(nome, ano_nascimento)
        self._cursos_oferecidos = ['ADM', 'TI', 'RH', 'Marketing', 'ADS']
        self.validaCurso(curso)
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        self.validaCurso(novo_curso)
        self._curso = novo_curso

    def validaCurso(self, curso):
        if curso in self._cursos_oferecidos:
            return True
        raise PermissionError(f'Curso {curso} não consta na lista de cursos')

    def addCursosOferecidos(self, nome_curso:str):
        self._cursos_oferecidos.append(nome_curso)
        print('Curso adicionado na lista de cursos oferecidos')


aluno = Aluno('Gustavo Marcello', 1996, 'ADM')
aluno.addCursosOferecidos('MED')
aluno.curso = 'MED'
print(aluno.__dict__)