letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

try:
    choice = int(input("1. Зашифровать\n2. Расшифровать\n"))
    if choice == 1:
        a = input("Введите сообщение для шифровки (латиницей): ")
        key = int(input("Введите ключ  для шифрования(от -25 до 25): "))  #
        a = a.lower()
        c = ""
        for letter in a:
            p = letters.find(letter)
            p1 = p + key
            if letter in letters:
                c = c + letters[p1]

            else:
                c = c + letter
        print("Зашифровано: ", c)
    if choice == 2:
        a = input("Введите сообщение для расшифровки (латиницей): ")
        key = int(input("Введите ключ  для расшифровки(от -25 до 25): "))  #
        a = a.lower()
        c = ""
        for letter in a:
            p = letters.find(letter)
            p1 = p - key
            if letter in letters:
                c = c + letters[p1]

            else:
                c = c + letter
        print("Расшифровано: ", c)
    else:
        quit("Ошибка! Команда не найдена! Перезапустите программу!")
except ValueError:
    print('Ошибка! Введено не число!')
