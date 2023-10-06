from config import config
from commands import Find

prefix_find = config["find"]["px"]
prefix_find_replace = config["find_replace"]["px"]

prueba = Find.Find("texto.txt")
# print(prueba.search("algorithms"))
print(prueba.set_search("al[abc]goritms", 2))