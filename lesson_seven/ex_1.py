from random import randrange

f = 'ex_1'
count_line = 5


def write(num, name):
    fail = open(name, 'a', encoding='utf-8')
    while num > 0:
        x = int(randrange(-1000, 1000))
        y = float(randrange(-1000, 1000))
        fail.write(f'{x} / {y} \n')
        num -= 1
    fail.close()


write(count_line, f)
