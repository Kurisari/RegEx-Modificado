from config import config
from commands import Find
from commands import Find_replace
from events import Identifier

prefix_find = config["find"]["px"]
prefix_find_replace = config["find_replace"]["px"]

user_input = ""
while user_input != " ":
    user_input = input()
    Identify = Identifier.Identifier(user_input)
    replace = Identify.replaceIdentifier()
    Range = Identify.symbol_finder(user_input, 0, 45)
    Set = Identify.symbol_finder(user_input, 0, 91)
    Asterisk = Identify.symbol_finder(user_input, 0, ord(config["global"]["any_letter"]))
    Question = Identify.symbol_finder(user_input, 0, ord(config["global"]["appear"]))
    Or = Identify.symbol_finder(user_input, 0, ord(config["global"]["or"]))
    Key = Identify.symbol_finder(user_input, 0, 123)
    if replace:
        find_replace = Find_replace.Find("texto.txt")
    else:
        find = Find.Find("texto.txt")
        if Range:
            print("Rango")
            pattern = Identify.identify_pattern(user_input, 2)
            bracket_idx = Identify.symbol_finderI(user_input, 0, 91) - 2
            print(find.range_search(pattern, bracket_idx))
        if Set and not Range:
            print("Conjunto")
            pattern = Identify.identify_pattern(user_input, 2)
            bracket_idx = Identify.symbol_finderI(user_input, 0, 91) - 2
            print(find.set_search(pattern, bracket_idx))
        if Asterisk:
            print("Asterisco")
            pattern = Identify.identify_pattern(user_input, 2)
            print(find.all_char_search(pattern))
        if Question:
            print("Pregunta")
            pattern = Identify.identify_pattern(user_input, 2)
            print(find.question_search(pattern))
        if Or:
            print("O")
            pass
        if Key:
            print("Repeticion")
            pattern = Identify.identify_pattern(user_input, 2)
            key_idx = Identify.symbol_finderI(user_input, 0, 123) - 2
            print(find.key_search(pattern, key_idx))
        if not Range and not Set and not Asterisk and not Question and not Or and not Key:
            pattern = Identify.identify_pattern(user_input)
            print(find.search(pattern))
        
    