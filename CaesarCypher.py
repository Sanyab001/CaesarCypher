alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
fin_alph = []

try:
    number = int(input("Укажите сдвиг: "))
    msg = input("Введите слово для шифрования: ").upper()

    for i in range(number, len(alph)):
        fin_alph.append(alph[i])
    for i in range(number):
        fin_alph.append(alph[i])


    def crypter():
        f_msg = ''
        for i in range(len(msg)):
            for n in range(len(alph)):
                if msg[i] == alph[n]:
                    f_msg = f_msg + (fin_alph[n])
                else:
                    pass
        return f_msg


    print(crypter())

except (ValueError, IndexError):
    print("Указано неверное значение!")
    exit()
