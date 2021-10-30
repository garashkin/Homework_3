int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
print(' _ '.join(map(int_func, input("Введите фразу: ").split())))