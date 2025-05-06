class Servico:
    def __init__(self, id_servico, nome, preco, comissao):
        self.id_servico = id_servico
        self.nome = nome
        self.preco = preco
        self.comissao = comissao

    def calcular_comissao(self, funcionario):
        comissao = self.preco * funcionario.comissao
        return comissao

    def cadastrar_servico(self, database, funcionario):
        try:
            comissao = self.comissao
            database.inserir_servico(self.nome, self.preco, comissao)
            print("Serviço cadastrado com sucesso.")
        except Exception as e:
            print(f"Erro ao cadastrar serviço: {str(e)}")

    def inserir_servico(self, database):
        with database.obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO servicos (nome, preco, comissao) VALUES (?, ?, ?)",
                           (self.nome, self.preco, self.comissao))
            conexao.commit()

    def deletar_servico(self, database):
        try:
            database.deletar_servico(self.nome)
            print("Serviço excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir serviço: {str(e)}")

    @staticmethod
    def obter_servicos(database):
        with database.obter_conexao() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM servicos")
            servicos = cursor.fetchall()
        return [Servico(servico[0], servico[1], servico[2]) for servico in servicos]

    def __str__(self):
        return f"Nome: {self.nome}\nPreço: R$ {self.preco:.2f}"

