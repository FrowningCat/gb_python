from typing import Dict


def fun(x, y, number_attempt):
    mistic(x, y)
    attempt = 0
    while attempt < number_attempt:
        t = input("Введите отгадку: ")
        answer = y.split(" ")
        for i in range(len(answer)):
            if t == answer[i]:
                print(f"Вы угадали с {attempt + 1} попытки")
                res(x, attempt)
                exit()
        attempt += 1
    print("0")


def mistic(x, y):
    tuple = {x: y}
    print(tuple)


def res(x, attempt):
    _res: Dict = {}
    _res[x] = attempt + 1
    print(_res)
