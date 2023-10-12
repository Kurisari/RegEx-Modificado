from config import config
class FindReplace:
    def __init__(self, filename):
        self.ALPHABET_SIZE = config["global"]["ALPHABET_SIZE"]
        self.filename = filename
    
    def __char_to_index(self, char):
        return ord(char)
    
    def __calculate_bad_match_table(self, pattern):
        p = len(pattern)
        bad = [p]*self.ALPHABET_SIZE
        for k in range(p - 1):
            bad[self.__char_to_index(pattern[k])] = p - k - 1
        return bad
    
    def __symbol_finder(self, pattern, start, ascii):
        for i in range(start, len(pattern)-1):
            curr = self.__char_to_index(pattern[i])
            if curr == ascii:
                return i
        return
    
    def search(self, pattern, replace, flag1, flag2):
        if pattern == "":
            return
        matches = []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            if flag1 == "i" or flag2 == "i":
                lines = [line.lower() for line in lines]
                pattern = pattern.lower()
            line_num = 0
            for current_line in lines:
                line_num += 1
                bad_match_table = self.__calculate_bad_match_table(pattern)
                patt_size = len(pattern)
                text_idx = patt_size - 1
                while text_idx < len(current_line):
                    shared_substr = 0
                    while shared_substr < patt_size:
                        if current_line[text_idx - shared_substr] == pattern[patt_size - shared_substr - 1]:
                            shared_substr += 1
                        else:
                            break
                    if shared_substr == patt_size:
                        current_line = current_line[:text_idx - patt_size + 1] + replace + current_line[text_idx + 1:]
                        if flag1 == config["global"]["global_flag"] or flag2 == config["global"]["global_flag"]:
                            matches.append((line_num, text_idx - patt_size + 1))
                        else:
                            matches.append((line_num, text_idx - patt_size + 1))
                            lines[line_num - 1] = current_line
                            file.writelines(lines)
                            return matches
                    text_idx += bad_match_table[ord(current_line[min(text_idx, len(current_line) - 1)])]
                lines[line_num - 1] = current_line
                if flag1 == "i" or flag2 == "i":
                    current_line = current_line.lower()
            file.writelines(lines)
        return matches
    
    def set_search(self, pattern, bracket_idx, flag1, flag2):
        end_bracket_idx = self.__symbol_finder(pattern, bracket_idx, 93)
        first_part = pattern[:bracket_idx]
        set_part = pattern[bracket_idx + 1: end_bracket_idx]
        second_part = pattern[end_bracket_idx+1:]
        words = []
        matches = []
        for i in range(len(set_part)):
            words.append(first_part + set_part[i] + second_part)
        for i in range(len(words)):
            matches.append(self.search(words[i], flag1, flag2))
        return matches
    
    def range_search(self, pattern, bracket_idx, flag1, flag2):
        end_bracket_idx = self.__symbol_finder(pattern, bracket_idx, 93)
        first_part = pattern[:bracket_idx]
        second_part = pattern[end_bracket_idx+1:]
        words = []
        matches = []
        for i in range(self.__char_to_index(pattern[bracket_idx+1]), self.__char_to_index(pattern[end_bracket_idx-1])+1):
            words.append(first_part + chr(i) + second_part)
        for i in range(len(words)):
            matches.append(self.search(words[i], flag1, flag2))
        return matches
    
    def all_char_search(self, pattern, flag1, flag2):
        asterisk_idx = self.__symbol_finder(pattern, 0, 42)
        first_part = pattern[:asterisk_idx]
        second_part = pattern[asterisk_idx+1:]
        words = []
        matches = []
        for i in range(97, 123):
            words.append(first_part + chr(i) + second_part)
        for i in range(len(words)):
            matches.append(self.search(words[i], flag1, flag2))
        return matches
    
    def or_search(self, pattern, flag1, flag2):
        bar_idx = self.__symbol_finder(pattern, 0, 124)
        first_pattern = pattern[:bar_idx-1]
        second_pattern = pattern[bar_idx+2:]
        matches = []
        matches.append(self.search(first_pattern, flag1, flag2))
        matches.append(self.search(second_pattern, flag1, flag2))
        return matches
    
    def key_search(self, pattern, key_idx, flag1, flag2):
        end_key_idx = self.__symbol_finder(pattern, 0, 125)
        first_part = pattern[:key_idx-1]
        number = pattern[key_idx+1:end_key_idx]
        second_part = pattern[end_key_idx+1:]
        number = (int)(number)
        word = first_part + pattern[key_idx-1]*number + second_part
        matches = []
        matches.append(self.search(word, flag1, flag2))
        return matches
    
    def question_search(self, pattern, flag1, flag2):
        question_idx = self.__symbol_finder(pattern, 0, 63)
        first_part = pattern[:question_idx]
        second_part = pattern[question_idx+1:]
        matches = []
        matches.append(self.search(first_part + second_part, flag1, flag2))
        matches.append(self.search(first_part[:-1] + second_part, flag1, flag2))
        return matches