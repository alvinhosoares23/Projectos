def decorator(funcao):
    def envelope(*args, **kwargs):
        print("operacao 1....")
        resultado = funcao(*args,**kwargs)
        print('operacao 2 ...')
        return resultado
    return envelope

@decorator
def ola_mundo(var1):
    print(f'Ola Mundo {var1} ...')
    return var1

ola_mundo("Matrix")