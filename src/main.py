from config import config
from commands import Find

prefix_find = config["find"]["px"]
prefix_find_replace = config["find_replace"]["px"]

prueba = Find.Find("algorithm", "texto.txt")
print(prueba.search())