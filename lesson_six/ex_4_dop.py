def fun(date, month, year):
    if (0 < year < 10000) and (0 < month < 13) and (0 < date < 32):
        print(True)
    else:
        print(False)
    _leap_year(year)


def _leap_year(year):
    if year % 4 == 0:
        print(True)
    else:
        print(False)
