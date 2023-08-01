import os.path

str = "C:/Users/Admin/Desktop/Утилиты/Новая папкa/wow.png"

def fun(str):
    *way, fulname = os.path.split(str)
    name, expansion = fulname.split(".")
    tuple = (way, name, expansion)
    print(tuple)


fun(str)
