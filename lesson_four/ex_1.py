string = str(input("Введите строку: "))


def func(str):
    word = str.split()
    for i, item in enumerate(word, 1):
        print(f'{i} {item:>{len(max(word, key=len))}}')


func(string)
