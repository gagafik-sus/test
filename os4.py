print("загрузка библиотек")
import os
import time
import random
import sys
from datetime import datetime
print("загрузка shell")

def shell():
    while True:
        shellcommand = input('Adubam Shell v0.2 -$ ')

        if shellcommand == "q":
            print('command: exit (q)')
            time.sleep(1)
            os.system('clear')
            print('выход из системы')
            time.sleep(0.3)
            os.system('clear')
            print('выход из системы..')
            time.sleep(0.3)
            os.system('clear')
            print('выход из системы...')
            time.sleep(0.3)
            os.system('clear')
            print('выход из системы....')
            time.sleep(0.3)
            os.system('clear')
            break

        elif shellcommand == "clear":
            os.system('clear')

        elif shellcommand == "calc":
            print('adubam calc v0.2')
            print('Введите пример (например: 2 + 2)')
            primer = input("calc shell: ")
            allowed_chars = "0123456789+-*/. ()"
            is_safe = all(char in allowed_chars for char in primer)

            if is_safe and primer.strip() != "":
                try:
                    result = eval(primer)
                    print("= " + str(result))
                except:
                    print("ошибка в примере")
            else:
                print("можно писать только - ", allowed_chars)

        elif shellcommand == "help":
            print("""
commands:
help  - помощь
calc  - калькулятор
q     - выход
clear - очистка
system - комманды системы (beta)
fetch - информация о системе
host - на чём работает эта штука
clock - часы (beta)
            """)
            print("mods:")
            os.system('ls mods')

        elif shellcommand == "system":
            print('error: type system help')

        elif shellcommand == "system help":
            print( """
commands system:
help - help
shell - system shell (bash, fish, zsh)
                  """)

        elif shellcommand == "system shell":
            print("enter your system command. например: sudo rm -rf /*")
            yshell = input("type your command (you can write bash to use):  ")
            print("your command - ", yshell)
            os.system(yshell)

        elif shellcommand == "fetch":
            print()
            print("|========|")
            time.sleep(0.1)
            print("|AdubamOS|   AdubamOS v0.4modified")
            time.sleep(0.1)
            print("|( 0)(0 )|   Adu-Shell v0.2r")
            time.sleep(0.1)
            print("|   --   |   r - release")
            time.sleep(0.1)
            print("|========|   b - beta")
            print()

        elif shellcommand == "host":
            os.system("uname -s")

        elif shellcommand == "clock":
            now = datetime.now()
            print(now.strftime("%H:%M:%S"))

        elif os.path.exists(f"mods/{shellcommand}.py"):
            exec(open(f"mods/{shellcommand}.py").read())

        else:
            print(shellcommand, " - комманда не найдена type - help")

print('done')
time.sleep(0.1)
text = "Hello!"
current = ""
for char in text:
    current += char
    os.system('clear')
    print(current)
    time.sleep(0.2)

print('welcome to')
time.sleep(1)

nameos = "AdubamOS"
oscur = ""
for ch in nameos:
    oscur += ch
    oscur += "" # Заглушка
    os.system('clear')
    print(oscur)
    time.sleep(0.1)

time.sleep(0.5)
os.system('clear')

print('AdubamOS v0.4 modified')
time.sleep(0.1)
print("""
    |========|
    |AdubamOS|
    |( 0)(0 )|
    |   --   |
    |========|
(modified)

    """)
shell()

