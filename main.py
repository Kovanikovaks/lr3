
wor = []
while (new := str(input())) != "stop":
    wor.append(new)
print(' '.join(wor))


def proc1():

 a = input()
 if ('ф' or 'Ф') in a:
    print('слово  редкое')
 else:
    print('слово не редкое')

proc1()

def proc2():
 from random import randint
 n = 0
 print("Для завершения игры введите слово стой")
 while True:

    chix1 = randint(1, 10)
    chix2 = randint(1, 10)
    print(f"{chix1} + {chix2} = ", end="")
    resul = input()

    if resul == "stop":
        break
    resul = int(resul)
    if chix1 + chix2 == resul:
        print("Правильно!")
    else:
        print("Ответ неправильный :(")
        n += 1
    if n == 3:
        print("Game over!")
        break

proc2()

