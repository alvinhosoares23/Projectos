class Conta:
    def __init__(self,n_conta,titular,data,saldo = 0):
        self.__n_conta=n_conta
        self.__titular =titular
        self._data = data
        self.__saldo = saldo
    def __str__(self) -> str:
        return f"{__class__.__name__} : {self.__n_conta, self.__titular,self._data,self.__saldo }"

    def deposito(self, valor):
        self.__saldo += valor
        print(f'deposito de {self.__saldo} Efectuada com sucesso!')
        
    def levantamento (self, valor):
        self.__saldo -= valor
        print(f'{self.__saldo} Levantado com sucesso!')
    
    def consulta (self):
        print(f'Saldo:{self.__saldo}')

c1= Conta('124896','Carlos F', '24/05/2024')
print(c1)
c1.deposito(80000)
c1.consulta()
c1.levantamento(5000)
c1.consulta()