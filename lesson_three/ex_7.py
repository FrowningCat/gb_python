text = str(input("Введите строку текта: "))
i = 0
dict = {}
letter = ""

while i < len(text):
    letter = text[i]
    x = 0
    count = 0
    while x < len(text):
        if letter == text[x]:
            count += 1
        x += 1
    dict[letter] = count
    i += 1

print(dict)
