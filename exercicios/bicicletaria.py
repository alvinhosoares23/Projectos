class Bicicletas:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor

    def buzinar(self):
        print('Prim Prim Prim !!!!')

    def parar(self):
        print("Prando bicicleta !!!")
        print("Bicicleta Parado !!!")

    def trocar_marcha(self,num_marcha):
        print(f"Marcha Trocada para {num_marcha}")
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items() ])} "

b1 = Bicicletas('Azul', 'Montan Dragon','2007', 30000)
print(b1)