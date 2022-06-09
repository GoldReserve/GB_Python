# Cоздаем файлик с текстом
import datetime

f = open('Log.txt', 'w+', encoding='utf8')

def write_log(txt:str):
    f = open('Log.txt', 'a', encoding='utf8')
    f.write(f"{datetime.datetime.now()} ----- {txt}, \n")
    print()
    f.close()
    return

