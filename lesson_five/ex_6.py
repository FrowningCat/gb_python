g = (f'\n' if j == 6 else f'{j:2d} * {i:} = {i * j:2d}' for i in range(2, 10) for j in range(2, 7))
g_2 = (f'\n' if j == 10 else f'{j:2d} * {i:} = {i * j:2d}' for i in range(2, 10) for j in range(6, 11))
print(*g)
print(*g_2)