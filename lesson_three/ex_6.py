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

new_list.sort()

for i, item in enumerate(new_list, 1):
    print(f'{i} {item:>{len(max(new_list, key=len))}}')
