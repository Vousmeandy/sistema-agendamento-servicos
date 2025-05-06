from datetime import datetime
from agendamento import Agendamento
from BancoDeDados import Database
from cliente import Cliente
from funcionario import Funcionario
from servico import Servico


def menu_principal():
    print("1. Cadastrar cliente")
    print("2. Cadastrar funcionário")
    print("3. Cadastrar serviço")
    print("4. Agendar")
    print("5. Sair")


def cadastrar_cliente(database):
    print("Cadastro de Cliente")
    id_cliente = int(input("ID do cliente: "))
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    numero_telefone = input("Número de Telefone: ")
    quantidade_atendimentos = int(input("Quantidade de Atendimentos: "))
    cliente = Cliente(id_cliente, nome, cpf, data_nascimento, numero_telefone, quantidade_atendimentos)
    cliente.cadastrar_cliente(database)


def cadastrar_funcionario(database):
    print("Cadastro de Funcionário")
    id_funcionario = int(input("ID do funcionário: "))
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    comissao = float(input("Comissão: "))
    funcionario = Funcionario(id_funcionario, nome, cpf, data_nascimento, comissao)
    funcionario.cadastrar_funcionario(database)


def cadastrar_servico(database):
    id_servico = (input("digite o id do serviço"))
    nome = input("Digite o nome do serviço: ")
    preco = float(input("Digite o preço do serviço: "))
    comissao = float(input("Digite a comissão do serviço: "))
    servico = float (Servico(nome, preco, comissao))

    # Inserir o serviço no banco de dados
    database.inserir_servico(servico)

    print("Serviço cadastrado com sucesso.")
def realizar_agendamento(database):
    id_servico = int(input("ID do serviço: "))
    id_cliente = int(input("ID do cliente: "))
    id_funcionario = int(input("ID do funcionário: "))
    data = input("Data (dd/mm/aaaa): ")
    horario = input("horario: ")
    agendamento = Agendamento(id_servico, id_cliente, id_funcionario, data, horario)
    agendamento.agendar(database)


def main():
    database = Database("clientes.db", "agendamentos.xlsx")
    database.criar_tabelas()

    while True:
        menu_principal()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            cadastrar_cliente(database)
        elif opcao == "2":
            cadastrar_funcionario(database)
        elif opcao == "3":
            cadastrar_servico(database)
        elif opcao == "4":
            realizar_agendamento(database)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")


if __name__ == "__main__":
    main()
