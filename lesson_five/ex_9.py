name = ["Влад", "Олег", "Игорь"]
percent = ["5.15", "10.25", "7.5"]
salary = [4000, 5000, 3000]

print({name:  float(percent) * salary for name, percent, salary in zip(name, percent, salary)})
