list = input("Введите данные")
result = None

if list.isdigit():
    result = int(list)
elif (list.count(".") == 1 or list.startswith("-")):
    result = float(list)
elif not list.islower():
    result = list.lower()
else:
    result = list.upper()

print(result)
