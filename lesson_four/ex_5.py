name = ["Влад", "Олег", "Игорь"]
percent = ["5.15", "10.25", "7.5"]
salary = [4000, 5000, 3000]


def fun(name, percent, salary):
    result = {}
    for i in range(0, len(name)):
        cash = float(percent[i]) * float(salary[i])
        result[name[i]] = cash
    print(result)


fun(name, percent, salary)
