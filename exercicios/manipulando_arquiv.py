import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

arquivo = open(ROOT_PATH / "arq.txt","r")
arquivo.close()
os.mkdir(ROOT_PATH / "Nava Pasta")
# os.rename(ROOT_PATH / "arq.txt", ROOT_PATH / "arqv.txt")
# os.remove( ROOT_PATH /"arq.txt")
# shutil.move(ROOT_PATH /"arq.txt", ROOT_PATH /"Nava Pasta" / "arq.txt")
#