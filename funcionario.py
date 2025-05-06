from pessoa import Pessoa
from BancoDeDados import Database

class Funcionario(Pessoa):
    def __init__(self, id_funcionario, nome, cpf, data_nascimento, comissao):
        super().__init__(nome, cpf, data_nascimento)
        self.id_funcionario = id_funcionario
        self.comissao = comissao

    def cadastrar_funcionario(self, database):
        query = "INSERT INTO funcionarios (nome, cpf, data_nascimento, comissao) VALUES (?, ?, ?, ?)"
        parametros = (self.nome, self.cpf, self.data_nascimento, self.comissao)
        database.executar_query(query, parametros)
        print("Funcionário cadastrado com sucesso!")

    def inserir_funcionario(self, cpf, nome, data_nascimento, salario, comissao):
        query = "INSERT INTO funcionarios (nome, cpf, data_nascimento, salario, comissao) VALUES (?, ?, ?, ?, ?)"
        parametros = (nome, cpf, data_nascimento, salario, comissao)
        database.executar_query(query, parametros)
        print("Funcionário cadastrado com sucesso.")

    def excluir_funcionario(self, database):
        query = "DELETE FROM funcionarios WHERE id_funcionario = ?"
        parametros = (self.id_funcionario,)
        database.executar_query(query, parametros)
        print("Funcionário excluído com sucesso!")
