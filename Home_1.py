def s_calc(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Делить на ноль нельзя')

print(s_calc(int(input('Введите первое число: ')), int(input('Введите второе число: '))))