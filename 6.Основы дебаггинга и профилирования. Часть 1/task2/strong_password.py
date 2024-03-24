dict = {}

def is_strong_password(password: str) -> bool:

    if not dict:
        with open('words.txt', 'r') as file:
            for word in file:
                word = word.strip()
                if len(word) > 4:
                    dict.setdefault(len(word), [])
                    dict[len(word)].append(word)

    password = password.lower()
    for i in range(4, len(password)):
        if i in dict.keys():
            for word in dict[i]:
                if word.lower() in password:
                    return False

    return True


if __name__ == "__main__":
    print(is_strong_password('PaSsWoRd'))
    print(is_strong_password('PaSsWoRdname'))
    print(is_strong_password('kdjgskdnsk'))