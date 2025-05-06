from datetime import datetime
import sqlite3
import openpyxl
from BancoDeDados import Database

class Agendamento:
    def __init__(self, data, horario, id_cliente, id_servico):
        self.data = data
        self.horario = horario
        self.id_cliente = id_cliente
        self.id_servico = id_servico

    def agendar(self, database):
        query = "INSERT INTO agendamentos (data, horario, id_cliente, id_servico) VALUES (?, ?, ?, ?)"
        parametros = (self.data, self.horario, self.id_cliente, self.id_servico)
        database.executar_query(query, parametros)

    def validar_data_hora(self, data_hora):
        try:
            data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        except ValueError:
            raise ValueError("Formato de data e hora inválido. O formato deve ser dd/mm/aaaa hh:mm.")

        return data_hora

    def buscar_cliente(self, cpf):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM clientes WHERE cpf=?", (cpf,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            raise ValueError("Cliente não encontrado.")

        return result[0]

    def buscar_funcionario(self, id_funcionario):
        conn = sqlite3.connect("funcionarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM funcionarios WHERE id_funcionario=?", (id_funcionario,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            raise ValueError("Funcionário não encontrado.")

        return result[0]

    def verificar_agendamentos(self):
        # Abrir o arquivo Excel
        workbook = openpyxl.load_workbook("agendamentos.xlsx")
        sheet = workbook.active

        # Verificar se existem agendamentos para o mesmo horário
        for row in sheet.iter_rows(min_row=2):
            data_hora_agendamento = row[3].value
            if data_hora_agendamento == self.data_hora:
              raise ValueError("Já existe um agendamento para o mesmo horário.")

        workbook.close()

    def agendar(self):
        self.verificar_agendamentos()

        # Adicionar o agendamento ao banco de dados
        database = Database()
        database.conectar()
        self.id_cliente = self.buscar_cliente(self.id_cliente)
        self.id_funcionario = self.buscar_funcionario(self.id_funcionario)
        self.data_hora = f"{self.data} {self.horario}"
        self.validar_data_hora(self.data_hora)

        self.agendar(database)
        database.desconectar()

    def __str__(self):
        return f"Agendamento: {self.descricao}\nCliente: {self.cliente}\nFuncionário: {self.funcionario}\nData e Hora: {self.data_hora}\nServiço: {self.servico}"
