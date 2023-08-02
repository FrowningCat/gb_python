def fun(x, y, z):
    u = 0
    while u < z:
        t = input("Введите отгадку: ")
        tt = y.split(" ")
        for i in range(len(tt)):
            if t == tt[i]:
                print(f"Вы угадали с {u + 1} попытки")
                exit()
        u += 1

    print("0")
