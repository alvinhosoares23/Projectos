import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
'''
try :
    with open(ROOT_PATH / "arqv.csv", "a",newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id','nome','idade'])
        escritor.writerow(['1','carlos','29'])
        escritor.writerow(['2','Carla','27'])
        escritor.writerow(['3','Matrix','28'])

except Exception as ex:
    print(ex)
'''
try :
    with open(ROOT_PATH / "arqv.csv", "r",newline='', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

except Exception as ex:
    print(ex)