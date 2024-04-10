from abc import ABC, abstractmethod
from datetime import datetime

class ContaBancaria(ABC):
    def __init__(self, saldo_inicial=0, limite_saque=500, max_saques=3):
        self.saldo = saldo_inicial
        self.limite_saque = limite_saque
        self.max_saques = max_saques
        self.saques_realizados = 0
        self.depositos = []
        self.saques = []
        self.ultimo_dia = datetime.now()

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append((valor, datetime.now()))

    def saque(self, valor):
        hoje = datetime.now()
        
        if hoje != self.ultimo_dia:
            self.saques_realizados = 0
            self.ultimo_dia = hoje
        
        if self.saldo >= valor and valor <= self.limite_saque and self.saques_realizados < self.max_saques:
            self.saldo -= valor
            self.saques.append((valor, datetime.now()))
            self.saques_realizados += 1
            print(f"#  Saque de {valor} Realizado com sucesso")
        else:
            print("#######################################")
            print("#  Não foi possível realizar o saque. #")
            print("#  Obs(Só é permito 3 saques por dia) #")
            print("#          e Limite maximo de 500R$   #")

    def extrato(self):
        print("Extrato:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"# Depósito: R$ {deposito[0]:.2f} - Data: {deposito[1]}")
            for saque in self.saques:
                print(f"# Saque: R$ {saque[0]:.2f} - Data: {saque[1]}")

        print(f"# Saldo atual: R$ {self.saldo:.2f}")
           
class ContaCorrente(ContaBancaria):
    pass


class Cliente(ABC):
    def __init__(self, nome):
        self.nome = nome

class PessoaFisica(Cliente):
    pass

class Transacao(ABC):
    def __init__(self):
        self.data_hora = datetime.now()

    @abstractmethod
    def executar(self):
        pass

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Deposito(Transacao):
    def __init__(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def executar(self):
        self.conta.deposito(self.valor)

class Saque(Transacao):
    def __init__(self, conta, valor):
        self.conta = conta
        self.valor = valor

    def executar(self):
        self.conta.saque(self.valor)

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    print("#-----------------------------------------------------#")
    print(f"#   Usuário {nome} criado com sucesso!")
    return nome


def criar_conta_corrente(usuario):
    print(f"#   Conta corrente criada para o usuário {usuario}.")
    print("#-----------------------------------------------------#")
    return ContaCorrente()

# Criação de usuário e conta corrente
usuario = criar_usuario()
conta = criar_conta_corrente(usuario)

# Menu interativo
while True:
    print('###################################')
    print("#     Escolha uma operação        #")
    print("#                                 #")
    print("#         1-> Depósito            #")
    print("#         2-> Saque               #")
    print("#         3-> Extrato             #")
    print("#         4-> Sair                #")
    print("#                                 #")
    print("###################################")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        deposito = Deposito(conta, valor_deposito)
        deposito.executar()
    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        saque = Saque(conta, valor_saque)
        saque.executar()
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")
