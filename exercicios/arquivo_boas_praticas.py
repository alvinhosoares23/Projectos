from pathlib import Path

ROOT_PATH = Path(__file__).parent

def ler_arquivo(arquivo):
    try:
        with open( ROOT_PATH /"arq.txt","r",encoding="utf-8") as arquivo:
            linha = arquivo.read()
    except Exception as ex:
        print(ex)
    return linha

def escrever_no_arquivo(aqrivo,valor):
    try:
        with open( ROOT_PATH /"arq.txt","a",encoding="utf-8") as arquivo:
            arquivo.writlines(valor)
    except Exception as ex:
        print(ex)
    
arqrivo  = open("E:/Docs/Projetos/exercicios/arq.txt","r")
valor = input("escreva o Texto : ")
escrever_no_arquivo(arqrivo,valor)
print(ler_arquivo(arqrivo))
