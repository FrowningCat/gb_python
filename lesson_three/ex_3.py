tuple = (1, "hello", True , 3.2)
dict = {}
i = 0

while i < len(tuple):
    if type(tuple[i]) == int:
        dict['int'] = tuple[i]
    elif type(tuple[i]) == str:
        dict['str'] = tuple[i]
    elif type(tuple[i]) == float:
        dict['flout'] = tuple[i]
    else:
        dict['bool'] = tuple[i]
    i += 1

print(dict)
