print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))
