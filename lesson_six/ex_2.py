from ex_2_dop import fun
from sys import argv

argument = map(int, argv[1:])
fun(*argument)
