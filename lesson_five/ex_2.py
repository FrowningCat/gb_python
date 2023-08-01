str = "Lorem ipsum dolor sit amet"
dict = ({i: ord(i) for i in str})
dict_it = iter(dict.items())

for i in range(5):
    print(next(dict_it))
