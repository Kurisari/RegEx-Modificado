from config import config

class Identifier:
    def __init__(self, user_input):
        self.user_input = user_input
        self.ALPHABET_SIZE = config["global"]["ALPHABET_SIZE"]
    
    def __char_to_index(self, char):
        return ord(char)
    
    def __search(self, pattern):
        if pattern == "":
            return
        matches = []
        for i in range(0, len(self.user_input)-len(pattern)+1):
            if self.user_input[i:i+len(pattern)] == pattern:
                matches.append(i)
        return matches
    
    def symbol_finder(self, pattern, start, ascii):
        for i in range(start, len(pattern)-1):
            curr = self.__char_to_index(pattern[i])
            if curr == ascii:
                return True
        return False
    
    def symbol_finderI(self, pattern, start, ascii):
        for i in range(start, len(pattern)-1):
            curr = self.__char_to_index(pattern[i])
            if curr == ascii:
                return i
        return
    
    def identify_pattern(self, user_input, start):
        aux = ""
        for i in range(start, len(user_input)):
            if user_input[i] == " ":
                break
            aux += user_input[i]
        user_input = aux
        return user_input
    
    def identify_or(self, user_input, start):
        aux = ""
        for i in range(start, len(user_input)):
            if user_input[i] == " " and user_input[i+1] != "|" and user_input[i-1] != "|":
                break
            aux += user_input[i]
        user_input = aux
        return user_input
    
    def replaceIdentifier(self):
        frSearch = self.__search("fr ")
        if len(frSearch) == 0:
            return False
        else:
            return True
    