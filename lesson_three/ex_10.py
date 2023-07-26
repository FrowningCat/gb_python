bag = {"map": 1, "water": 2, "knife": 1, "flashlight": 2, "tent": 10, "meal": 3, "thone": 1}
load_capacity = 8
yes = []

for kuch, value in bag.items():
    if value < load_capacity:
        load_capacity = load_capacity - value
        yes.append(kuch)

print(yes)
