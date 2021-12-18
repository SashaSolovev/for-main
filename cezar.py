letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" 
try:
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
    print("зашифровано: ", c)
except ValueError:
    print('Ошибка! Введено не число!')
  
