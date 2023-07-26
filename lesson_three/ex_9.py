text = str(input("Введите длииииииный текст: "))
text = text.split()
i = 0
list_words = []

while i < 10:
    word = ""
    x = 0
    t = 0
    number = 0
    # Находим самое часто повторяюшееся слово
    while x < len(text):
        if text.count(text[x]) > number:
            word = text[x]
            number = text.count(text[x])
        x += 1
    # Заносим слово в масив
    list_words.append(word)
    # Удоляем это слово из списка и проходим этот цикл еще 9 раз
    while t < len(text):
        text.remove(word)
        t += 1
    i += 1

print(list_words)
