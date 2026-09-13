from classes.pessoa import Pessoa
from classes.aluno import Aluno
from classes.professor import Professor
from classes.funcionario import Funcionario

def main():
    aluno = Aluno('Gustavo Marcello', 30, 'AdS', 'Fatec2021')
    professor = Professor('Maromo', 43, 'Programação', 'Mestre')
    funcionario = Funcionario('Felipinho', 21, 'Secretário', 'Secretaría')

    aluno.estudar()
    professor.estudar()
    funcionario.estudar()


if __name__ == '__main__':
    main()