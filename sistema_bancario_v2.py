from abc import ABC, abstractmethod
from datetime import datetime

class Log:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, descricao, valor):
        data_hora = datetime.now()
        data_formatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append((data_formatada, descricao, valor))

    def exibir_log(self):
        for transacao in self.transacoes:
            print(f"{transacao[0]} - {transacao[1]} - Valor: R${transacao[2]}")

class ContaIterator:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            return conta
        except IndexError:
            raise StopIteration



class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

class Pessoa(Cliente):
    def __init__(self, nome, cni, idade,endereco):
        super.__init__(endereco)
        self._nome = nome
        self.cni = cni
        self._idade = idade

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)

    @property
    def saldo(self):
        return float(self._saldo)
    @property
    def numero(self):
        return self._numero
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    def levantamento(self, valor:float):
        saldo = self.saldo
        if valor >= saldo:
            saldo -= valor
            print(f"Levantamento de {valor} efectuada")
            self.historico.adicionar_transacao()
            return True 
        else:
            print("Saldo insuficiente ....!") 
            return False
    def deposito(self, valor:float):
        saldo = self.saldo
        if valor > 0:
            saldo += valor
            print(f"deposito de {valor} efectuada")
            self.historico.adicionar_transacao()

        else:
            print("introduza o dinheiro...!")

class ContaCorrente(Conta):
    def __init__(self):
        self.limite = 20000
        self.limite_levantamentos = 10


class Transacao(ABC):
    @abstractmethod
    def adicionar_transacao(self, transacao: 'Transacao'):
        pass
class Historico:
    def adicionar_transacao(transacao :Transacao):
        pass

    def adicionar_transacao(self, conta: Conta):
        descricao = "Levatamento"
        conta.registrar_transacao(descricao, self.valor)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def adicionar_transacao(self, conta: Conta):
        descricao = "Depósito"
        conta.registrar_transacao(descricao, self.valor)

# Exemplo de uso:
cliente1 = Cliente("João", 30, "123456789", "Rua A", [])
conta1 = ContaCorrente(1000, 123, "001", cliente1, Log(), 2000, 10)
cliente1._contas.append(conta1)  # Adicionando conta ao cliente

print("Bem-vindo,", cliente1._nome)

while True:
    print("1. Consultar saldo")
    print("2. Fazer depósito")
    print("3. Fazer Levatamento")
    print("4. Exibir log de transações")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Saldo:", conta1.consulta())
    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: "))
        deposito = Deposito(valor)
        deposito.adicionar_transacao(conta1)
    elif opcao == "3":
        valor = float(input("Digite o valor do Levatamento: "))
        Levatamento = Levatamento(valor)
        Levatamento.adicionar_transacao(conta1)
    elif opcao == "4":
        print("Log de transações:")
        conta1.historico.exibir_log()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
