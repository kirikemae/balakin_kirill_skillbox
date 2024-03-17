import sys


def decrypt(s:str):
    result = []
    dots = 0

    for char in s:
        if char != '.':
            result.append(char)
            dots = 0
            continue

        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0

    return ''.join(result)

if __name__ == '__main__':
    data = sys.stdin.read()
    print(decrypt(data))