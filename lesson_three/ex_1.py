old_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
new_list = []
i = 0

while i < len(old_list):
    if new_list.count(old_list[i]) < 1:
        new_list.append(old_list[i])
    i += 1

print(new_list)
