alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
fin_alph = []
print("1 - зашифровать текст, 2 - расшифровать.")

try:
    ans = int(input("Выберите действие:"))

    if ans == 1:
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
    elif ans == 2:
        number = int(input("Укажите использованный ранее сдвиг:"))
        f_msg = input("Введите слово для дешифровки:").upper()

        for i in range(number, len(alph)):
            fin_alph.append(alph[i])
        for i in range(number):
            fin_alph.append(alph[i])


        def decrypter():
            s_msg = ''
            for i in range(len(f_msg)):
                for n in range(len(fin_alph)):
                    if f_msg[i] == fin_alph[n]:
                        s_msg = s_msg + (alph[n])
                    else:
                        pass
            return s_msg


        print(decrypter())


    else:
        print("Вы ввели неправильное число, выберите действие 1 или 2!")

except (ValueError, IndexError):
    print("Указано неверное значение!")
    exit()
