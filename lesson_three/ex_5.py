old_list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 9]
new_list = []
i = 1

for el in range(0, len(old_list)):
    if old_list[el] % 2 != 0:
        new_list.append(i)
    i += 1
    el += 1

print(new_list)
