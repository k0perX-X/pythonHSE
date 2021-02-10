from inputs_russian import int_input


def encrypt(s, key):
    new_s = ''
    for i in range(len(s)):
        new_s += chr((ord(s[i]) + key[i % len(key)]) % 1114112)
    return new_s


def decrypt(s, key):
    new_s = ''
    for i in range(len(s)):
        new_s += chr((ord(s[i]) - key[i % len(key)]) % 1114112)
    return new_s


def main():
    key = int_input(input_suggestion="Введите размер ключа шифрования: ", greater=0)
    key = [int_input(input_suggestion=f"Введите значение {i} элемента ключа шифрования: ", greater=0, less=1114111,
                     strictly_greater=False, strictly_less=False) for i in range(1, key + 1)]
    if int_input(input_suggestion="1 - Шифрование строки\n2 - Дешифрование строки\nВведите значение: ", greater=0,
                 less=3) == 1:
        print("Введите строку для шифрования: ")
        s = encrypt(input(), key)
        print(s)
        # print(decrypt(s, key))
    else:
        print("Введите строку для дешифрования: ")
        print(decrypt(input(), key))


if __name__ == '__main__':
    main()
