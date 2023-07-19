number_row = int(input("Сколько рядов у ёлки? "))
leng_tree_trunk = int(input("Какой длины ствол дерева? "))
number_needles = 1
needles = "*"
whitespace = " "
tree_trunk = "|"

while number_row > 0:
    print(whitespace * number_row, needles * number_needles)
    number_row -= 1
    number_needles += 2

while leng_tree_trunk > 0:
    print(whitespace * (number_row + 2), tree_trunk * (number_needles - 4))
    leng_tree_trunk -= 1
