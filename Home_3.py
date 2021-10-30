def my_func(var_1, var_2, var_3):
    print(f'Сумма двух наибольших аргументов равна: {var_1 + var_2 + var_3 - min([var_1, var_2, var_3])}')


my_func(
    int(input('аргумент 1: ')),
    int(input('аргумент 2: ')),
    int(input('аргумент 3: ')),
)