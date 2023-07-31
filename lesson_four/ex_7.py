company = {"OOO.ип": [1231, -4114, 4000], "OOO.зао": [-4321311, 1000, 424242, -43434],
           "OOO.ооо": [13123, -3123, 1231231, -31312, 31241, 3131, -97]}


def fun(company):
    for i in company:
        sallari = sum(company[i])
        if sallari < 0:
            print(False)
            exit()
    print(True)


fun(company)
