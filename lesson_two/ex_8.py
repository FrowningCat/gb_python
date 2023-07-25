old_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []
i = 0

while i < len(old_list):
    count = 0
    x = 0
    numer = old_list[i]
    while x < len(old_list):
        if numer == old_list[x]:
            count += 1
        x += 1
    if count > 1:
        if numer not in new_list:
            new_list.append(numer)
    i += 1

print(new_list)