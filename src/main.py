from config import config
from commands import Find
from commands import Find_replace
from events import Identifier

# User input variable
user_input = ""
# To exit the code " " is necessary
while user_input != " ":
    user_input = input()
    # The following lines are to identify the search case
    Identify = Identifier.Identifier(user_input)
    replace = Identify.replaceIdentifier()
    Range = Identify.symbol_finder(user_input, 0, 45)
    Set = Identify.symbol_finder(user_input, 0, 91)
    Asterisk = Identify.symbol_finder(user_input, 0, ord(config["global"]["any_letter"]))
    Question = Identify.symbol_finder(user_input, 0, ord(config["global"]["appear"]))
    Or = Identify.symbol_finder(user_input, 0, ord(config["global"]["or"]))
    Key = Identify.symbol_finder(user_input, 0, 123)
    # According to the char identified is the case and if it's repaced or not
    if replace:
        find_replace = Find_replace.FindReplace(config["global"]["text"])
        if Range and not Or:
            pattern = Identify.identify_pattern(user_input)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.range_search(pattern, replace, bracket_idx, flags[0], flags[1]))
        if Set and not Range and not Or:
            pattern = Identify.identify_pattern(user_input)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.set_search(pattern, replace, bracket_idx, flags[0], flags[1]))
        if Asterisk and not Or:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.all_char_search(pattern, replace, flags[0], flags[1]))
        if Question and not Or:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.question_search(pattern, replace, flags[0], flags[1]))
        if Or:
            pattern = Identify.identify_or(user_input)
            flags = Identify.identify_replace_or_flags(user_input)
            replace = Identify.identify_replace_or_word(user_input)
            print(find_replace.or_search(pattern, replace, flags[0], flags[1]))
        if Key and not Or:
            pattern = Identify.identify_pattern(user_input)
            key_idx = Identify.symbol_finderI(pattern, 123)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.key_search(pattern, replace, key_idx, flags[0], flags[1]))
        if not Range and not Set and not Asterisk and not Question and not Or and not Key:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_replace_flags(user_input)
            replace = Identify.identify_replace_word(user_input)
            print(find_replace.search(pattern, replace, flags[0], flags[1]))
    else:
        find = Find.Find(config["global"]["text"])
        if Range and not Or:
            pattern = Identify.identify_pattern(user_input)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_flags(user_input)
            print(find.range_search(pattern, bracket_idx, flags[0], flags[1]))
        if Set and not Range and not Or:
            pattern = Identify.identify_pattern(user_input)
            bracket_idx = Identify.symbol_finderI(pattern, 91)
            flags = Identify.identify_flags(user_input)
            print(find.set_search(pattern, bracket_idx, flags[0], flags[1]))
        if Asterisk and not Or:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_flags(user_input)
            print(find.all_char_search(pattern, flags[0], flags[1]))
        if Question and not Or:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_flags(user_input)
            print(find.question_search(pattern, flags[0], flags[1]))
        if Or:
            pattern = Identify.identify_or(user_input)
            flags = Identify.identify_or_flags(user_input)
            print(find.or_search(pattern, flags[0], flags[1]))
        if Key and not Or:
            pattern = Identify.identify_pattern(user_input)
            key_idx = Identify.symbol_finderI(pattern, 123)
            flags = Identify.identify_flags(user_input)
            print(find.key_search(pattern, key_idx, flags[0], flags[1]))
        if not Range and not Set and not Asterisk and not Question and not Or and not Key:
            pattern = Identify.identify_pattern(user_input)
            flags = Identify.identify_flags(user_input)
            print(find.search(pattern, flags[0], flags[1]))