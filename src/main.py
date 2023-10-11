from config import config
from commands import Find
from commands import Find_replace
from events import Identifier

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
        find_replace = Find_replace.FindReplace("texto.txt")
        if Range:
            print("Rango")
            pattern = Identify.identify_pattern(user_input, 3)
            bracket_idx = Identify.symbol_finderI(user_input, 0, 91) - 3
            print(find_replace.range_search(pattern, bracket_idx))
        if Set and not Range:
            print("Conjunto")
            pattern = Identify.identify_pattern(user_input, 3)
            bracket_idx = Identify.symbol_finderI(user_input, 0, 91) - 3
            print(find_replace.set_search(pattern, bracket_idx))
        if Asterisk:
            print("Asterisco")
            pattern = Identify.identify_pattern(user_input, 3)
            print(find_replace.all_char_search(pattern))
        if Question:
            print("Pregunta")
            pattern = Identify.identify_pattern(user_input, 3)
            print(find_replace.question_search(pattern))
        if Or:
            print("O")
            pattern = Identify.identify_or(user_input, 3)
            print(pattern)
            print(find_replace.or_search(pattern))
        if Key:
            print("Repeticion")
            pattern = Identify.identify_pattern(user_input, 3)
            key_idx = Identify.symbol_finderI(user_input, 0, 123) - 3
            print(find_replace.key_search(pattern, key_idx))
        if not Range and not Set and not Asterisk and not Question and not Or and not Key:
            pattern = Identify.identify_pattern(user_input, 3)
            print(find_replace.search(pattern))
    else:
        find = Find.Find("texto.txt")
        if Range:
            print("Rango")
            pattern = Identify.identify_pattern(user_input)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_flags(user_input)
            print(find.range_search(pattern, bracket_idx, flags[0], flags[1]))
        if Set and not Range:
            print("Conjunto")
            pattern = Identify.identify_pattern(user_input, 2)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_flags(user_input)
            print(find.set_search(pattern, bracket_idx, flags[0], flags[1]))
        if Asterisk:
            print("Asterisco")
            pattern = Identify.identify_pattern(user_input, 2)
            flags = Identify.identify_flags(user_input)
            print(find.all_char_search(pattern, flags[0], flags[1]))
        if Question:
            print("Pregunta")
            pattern = Identify.identify_pattern(user_input, 2)
            flags = Identify.identify_flags(user_input)
            print(find.question_search(pattern, flags[0], flags[1]))
        if Or:
            print("O")
            pattern = Identify.identify_or(user_input, 2)
            flags = Identify.identify_flags(user_input)
            print(find.or_search(pattern, flags[0], flags[1]))
        if Key:
            print("Repeticion")
            pattern = Identify.identify_pattern(user_input, 2)
            key_idx = Identify.symbol_finderI(pattern, 123)
            flags = Identify.identify_flags(user_input)
            print(find.key_search(pattern, key_idx, flags[0], flags[1]))
        if not Range and not Set and not Asterisk and not Question and not Or and not Key:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_flags(user_input)
            print(find.search(pattern, flags[0], flags[1]))