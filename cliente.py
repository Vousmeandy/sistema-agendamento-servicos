from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf, data_nascimento, numero_telefone, quantidade_atendimentos,):
        super().__init__(nome, cpf, data_nascimento)
        self.id_cliente = id_cliente
        self.numero_telefone = numero_telefone
        self.quantidade_atendimentos = quantidade_atendimentos
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def cadastrar_cliente(self, database):
        query = "INSERT INTO clientes (nome, cpf, data_nascimento, numero_telefone, quantidade_atendimentos) VALUES (?, ?, ?, ?, ?)"
        parametros = (self.nome, self.cpf, self.data_nascimento, self.numero_telefone, 0)  # Alteração na quantidade de atendimentos
        database.executar_query(query, parametros)
        print("Cliente cadastrado com sucesso!")

    def verificar_existencia_cliente(self, cpf, database):
        query = "SELECT COUNT(*) FROM clientes WHERE cpf = ?"
        parametros = (cpf,)
        resultado = database.executar_query_selecao(query, parametros)
        return resultado[0][0] > 0
