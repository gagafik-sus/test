import os
import time

def shell():
    while True:
        shellcommand = input('$ ')

        if shellcommand == "q":
            print('command: exit (q)')
            print('выход из системы через 3 секунды')
            time.sleep(3)
            break

        elif shellcommand == "clear":
            os.system('clear')

        elif shellcommand == "calc":
            print('adubam calc v0.1')
            print('введите свой пример. (2 + 2)')
            primer = input("calc shell 0.1: ")
            try:
                result = eval(primer)
                print("= " + str(result))
            except:
                print("ошибка в примере")

        elif shellcommand == "":
            print('adubam os v0.1')
            print('adubam shell v0.1')


        elif shellcommand == "help":
            print("""
commands:
help  - помощь
calc  - калькулятор
q     - выход
clear - очистка
            """)



text = "Hello!"
current = ""
for char in text:
    current += char
    os.system('clear')
    print(current)
    time.sleep(0.2)

print('welcome to')
time.sleep(1)

nameos = "ultra adubam os"
oscur = ""
for ch in nameos:
    oscur += ch
    os.system('clear')
    print(oscur)
    time.sleep(0.1)

print('adubam shell 0.1')
shell()
