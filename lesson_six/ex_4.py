from ex_4_dop import fun
from sys import argv

argument = map(int, argv[1:])
fun(*argument)
