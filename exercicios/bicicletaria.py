class Veiculo:
    def __init__(self,marca,modelo,rodas):
        self.__marca = marca
        self.__modelo =modelo
        self.__rodas = rodas

    def andar(self):
        print('Andando') 
    
    def parar(self):
        print(f"Parando {self.__class__.name} !!!")
        print(f"{self.__class__.name} Parado !!!")

class Bicicletas(Veiculo):
    def __init__(self,marca,modelo,rodas, cor, ano, marcha,valor):
        super().__init__(marca,modelo,rodas)
        self.cor = cor
        self.ano = ano 
        self.valor = valor
        self.marcha = marcha 
        self.velocidade = 0

    def buzinar(self):
        print('Prim Prim Prim !!!!')

    def aumentar_Velocidade(self):
        if self.velocidade < self.marcha:
            self.velocidade += 1 
            print(f"velocidade Aumentada para {self.velocidade}ª Marcha")
    
    def diminuir_velocidade(self):
        if self.velocidade > 1:
            self.velocidade -= 1 
            print(f"velocidade Dimimuida para {self.velocidade}ª Marcha")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items() ])} "

b1 = Bicicletas('Montan Dragon','Kirke',2,'Azul','2007',8, 30000)
print(b1)
b1.aumentar_Velocidade()
b1.andar()
b1.parar


