text = str(input("Введите длииииииный текст: "))
text = text.split()
i = 0
list_words = []

while i < 10:
    word = ""
    x = 0
    number = 0
    while x < len(text):
        if text.count(text[x]) > number:
            word = text[x]
            number = text.count(text[x])
        x += 1
    list_words.append(word)
    if word in text:
        text.remove(word)
    i += 1

print(list_words)
