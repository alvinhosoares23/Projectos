class Bicicletas:
    def __init__(self, cor, modelo, ano, marcha,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor
        self.marcha = marcha 
        self.velocidade = 0

    def buzinar(self):
        print('Prim Prim Prim !!!!')

    def parar(self):
        print("Prando bicicleta !!!")
        print("Bicicleta Parado !!!")

    def aumentar_Velocidae(self):
        if self.velocidade < self.marcha:
            self.velocidade += 1 
            print(f"velocidade Aumentada para {self.velocidade}ª Marcha")
    
    def diminuir_velocidade(self):
        if self.velocidade > 1:
            self.velocidade -= 1 
            print(f"velocidade Dimimuida para {self.velocidade}ª Marcha")
        

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items() ])} "

b1 = Bicicletas('Azul', 'Montan Dragon','2007',8, 30000)
print(b1)
b1.aumentar_Velocidae()