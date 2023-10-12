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
    
    def symbol_finderI(self, pattern, ascii):
        for i in range(len(pattern)-1):
            curr = self.__char_to_index(pattern[i])
            if curr == ascii:
                return i
        return
    
    def identify_pattern(self, user_input):
        aux = ""
        start = self.__begin_pattern_idx(user_input)
        for i in range(start, len(user_input)):
            if user_input[i] == " ":
                break
            aux += user_input[i]
        user_input = aux
        return user_input
    
    def __end_pattern_idx(self, user_input, start):
        for i in range(start, len(user_input)):
            if user_input[i] == " ":
                return i
        return len(user_input)
    
    def __begin_pattern_idx(self, user_input):
        for i in range(len(user_input)):
            if user_input[i] != " " and user_input[i-1] == " ":
                return i
        return i
    
    def identify_or(self, user_input):
        start = self.__begin_pattern_idx(user_input)
        aux = ""
        for i in range(start, len(user_input)):
            if user_input[i] == " " and user_input[i+1] != "|" and user_input[i-1] != "|":
                break
            aux += user_input[i]
        user_input = aux
        return user_input
    
    def __end_or(self, user_input):
        start = self.__begin_pattern_idx(user_input)
        for i in range(start, len(user_input)):
            if user_input[i] == " " and user_input[i+1] != "|" and user_input[i-1] != "|":
                return i
        return i
    
    def identify_flags(self, user_input):
        start = self.__begin_pattern_idx(user_input)
        end_pattern = self.__end_pattern_idx(user_input, start)
        flags = []
        for i in range(end_pattern, len(user_input)):
            if user_input[i] != " ":
                flags.append(user_input[i])
        if len(flags) == 0:
                flags = [""]*2
        if len(flags) == 1:
            flags.append("")
        return flags
    
    def identify_or_flags(self, user_input):
        end_pattern = self.__end_or(user_input)
        flags = []
        for i in range(end_pattern, len(user_input)):
            if user_input[i] != " ":
                flags.append(user_input[i])
        if len(flags) == 0:
                flags = [""]*2
        if len(flags) == 1:
            flags.append("")
        return flags
    
    def identify_replace_word(self, user_input):
        start = self.__begin_pattern_idx(user_input)
        end_pattern = self.__end_pattern_idx(user_input, start)
        new_input = user_input[end_pattern:]
        start_replace = self.__begin_pattern_idx(new_input)
        end_replace = self.__end_pattern_idx(new_input, start_replace)
        replace_word = new_input[start_replace:end_replace]
        return replace_word
    
    def identify_replace_flags(self, user_input):
        start = self.__begin_pattern_idx(user_input)
        end_pattern = self.__end_pattern_idx(user_input, start)
        new_input = user_input[end_pattern:]
        start_replace = self.__begin_pattern_idx(new_input)
        end_replace = self.__end_pattern_idx(new_input, start_replace)
        flags = []
        for i in range(end_replace, len(new_input)):
            if new_input[i] != " ":
                flags.append(new_input[i])
        if len(flags) == 0:
                flags = [""]*2
        if len(flags) == 1:
            flags.append("")
        return flags
    
    def identify_replace_or_word(self, user_input):
        end_pattern = self.__end_or(user_input)
        new_input = user_input[end_pattern:]
        start_replace = self.__begin_pattern_idx(new_input)
        end_replace = self.__end_pattern_idx(new_input, start_replace)
        replace_word = new_input[start_replace:end_replace]
        return replace_word
    
    def identify_replace_or_flags(self, user_input):
        end_pattern = self.__end_or(user_input)
        new_input = user_input[end_pattern:]
        start_replace = self.__begin_pattern_idx(new_input)
        end_replace = self.__end_pattern_idx(new_input, start_replace)
        flags = []
        for i in range(end_replace, len(new_input)):
            if new_input[i] != " ":
                flags.append(new_input[i])
        if len(flags) == 0:
                flags = [""]*2
        if len(flags) == 1:
            flags.append("")
        return flags
    
    def replaceIdentifier(self):
        frSearch = self.__search(config["find_replace"]["px"])
        if len(frSearch) == 0:
            return False
        else:
            return True
    