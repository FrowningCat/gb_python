from random import randint, choice

vowels = "euioay"
consonants = "wrtpsdfghklzcvnmb"


def name():
    len = int(input("Введите количсество псевдоимен: "))
    with open('ex_2', 'w') as file:
        for _ in range(len):
            print(generate_name(4, 7), file=file)


def generate_name(start, stop) -> str:
    return ''.join([choice(choice([vowels, consonants]))
                    for _ in range(randint(start, stop))]).capitalize()


name()
