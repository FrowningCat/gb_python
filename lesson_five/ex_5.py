print(*("Fizz" if i % 3 == 0 else "Buss" if i % 5 == 0 else "FizzBuss"
if i % 3 == i % 5 == 0 else i for i in range(0, 101, 2)))
