# RegEx-Modificado

This project, created for the Data Structures and Algorithms II course, customizes regular expressions (RegEx) functionality. The code allows pattern identification and manipulation in text, making it a valuable learning resource for string searching and manipulation algorithms.

## Authors

- [@Kurisari](https://www.github.com/kurisari)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## File Structure

- `config.py`: This file contains configuration settings in the form of dictionaries. It defines patterns, flags, and constants used in the code.

- `main.py`: This is the main script that takes user input, identifies patterns, and performs find or find-and-replace operations based on the input. It utilizes the other files for pattern identification and text manipulation.

- `Find.py`: This file contains a class called `Find`, which is responsible for searching for patterns in text files. It includes various search methods, such as range search, set search, asterisk search, question search, or search with flags.

- `Find_replace.py`: This file contains a class called `FindReplace`, which is responsible for searching and replacing patterns in text files. It includes methods for range search and replacement, set search and replacement, asterisk search and replacement, and more.

- `Identifier.py`: This file contains a class called `Identifier`, which helps identify patterns, flags, and replacement words in user input.

## How to Use

1. Start by configuring the patterns, flags, and constants in `config.py`. Modify the dictionary values as needed to fit your specific use case.

2. Run the `main.py` script. It will continuously prompt you for input.

3. Enter the pattern you want to search for, along with optional flags and replacement text if you want to perform a find-and-replace operation.

4. The code will identify the pattern, flags, and replacement text and perform the search or search-and-replace operation in the text file ("texto.txt" in this code).

5. The code will print the matches or the modified text based on the operation.

6. To exit the script, enter a space or any other termination condition you define in the loop.

## Additional Information

- The code supports various pattern types, including range, set, asterisk, question, or, key, and simple pattern searches.

- It also provides case-insensitive search functionality if configured in the flags.

- The Find and FindReplace classes have methods to handle different types of searches and replacements.

- When using or searches (denoted by '|'), make sure to provide both patterns and flags for each pattern. The code can perform separate searches for each pattern and return the results.

- Key searches allow you to specify a repetition count for a character in the pattern.

- Question searches allow for finding a pattern with or without the character preceding the question mark.

- The code supports searching for a pattern or performing find-and-replace operations.

## Running Tests

To run tests, run the following commands

```bash
  f regex g i
  [(1, 0), (5, 3), (10, 20)]
  f regex g
  [(1, 0), (10, 20)]
  f regex
  [(1, 0)]
  f reg?ex g i
  [[(1, 0), (5, 3), (10, 20)], [(3, 10), (3, 28)]]
  f reg?ex g
  [[(1, 0), (10, 20)], [(3, 10)]]
  f regex
  [[(1, 0)], [(3, 10)]]
  fr regex REGEX g i
  [(1, 0), (5, 3), (10, 20)]
```