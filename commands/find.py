from config import config
class Find:
    def __init__(self, pattern, filename):
        self.ALPHABET_SIZE = config["global"]["ALPHABET_SIZE"]
        self.pattern = pattern
        self.filename = filename

    def __char_to_index(self, char):
        return ord(char)

    def __calculate_bad_match_table(self):
        p = len(self.pattern)
        bad = [p]*self.ALPHABET_SIZE
        for k in range(p - 1):
            bad[self.__char_to_index(self.pattern[k])] = p - k - 1
        return bad

    def search(self):
        if self.pattern == "":
            return
        matches = []
        with open(self.filename, 'r') as file:
            current_line = file.readline()
            line = 0
            while current_line:
                line += 1
                bad_match_table = self.__calculate_bad_match_table()
                patt_size = len(self.pattern)
                text_idx = patt_size - 1  # Modificación aquí
                while text_idx < len(current_line):
                    shared_substr = 0
                    while shared_substr < patt_size:
                        if current_line[text_idx - shared_substr] == self.pattern[patt_size - shared_substr - 1]:
                            shared_substr += 1
                        else:
                            break
                    if shared_substr == patt_size:
                        matches.append((line, text_idx - patt_size + 1))
                    text_idx += bad_match_table[ord(current_line[min(text_idx, len(current_line) - 1)])]  # Modificación aquí
                current_line = file.readline()
        return matches
