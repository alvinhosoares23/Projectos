
def ler_arquivo(arquivo):
    arqrivo  = open("E:/Docs/Projetos/exercicios/arq.txt","r")
    arqrivo.close()
    linha = arquivo.read()
    arqrivo.close
    return linha

def escrever_no_arquivo(aqrivo,valor):
    arqrivo  = open("E:/Docs/Projetos/exercicios/arq.txt","a")
    arqrivo.writelines(f"{valor} \t \n")
    arqrivo.close()
    
arqrivo  = open("E:/Docs/Projetos/exercicios/arq.txt","r")
valor = input("escreva o Texto : ")
escrever_no_arquivo(arqrivo,valor)
print(ler_arquivo(arqrivo))
