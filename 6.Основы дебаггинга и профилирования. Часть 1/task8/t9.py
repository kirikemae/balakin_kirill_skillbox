from typing import List

letters = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

def my_t9(input: str) -> List[str]:
    letters_reversed = {i: j for j, i in letters.items()}
    result_words = []
    with open('words.txt', 'r', encoding='utf-8') as words:
        for word in words:
            word = word.strip()
            line_numbers = ''
            for letter in word[:len(input)]:
                for key in letters_reversed.keys():
                    if letter in key:
                        line_numbers += str(letters_reversed[key])
            if len(word) >= len(input) and input == line_numbers:
                result_words.append(word)
    return result_words


if __name__ == '__main__':
    numbers = input()
    t9 = my_t9(numbers)
    print(*t9)