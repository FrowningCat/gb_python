old_list = list(input("Введите строку текта: "))
new_list = []
text = ""
i = 0
old_list.append(" ")

while i < len(old_list):
    position = 0
    if old_list[i] != " ":
        text = text[position:] + old_list[i]
    else:
        new_list.append(text)
        text = ""
    i += 1

i = 0
new_list.sort()

while i < len(new_list):
    print(i + 1, new_list[i])
    i += 1
