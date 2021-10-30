def person(name, lastname, year_of_birth, city, email, telephone_number):
    return print(f'Имя: {name}, Фамилия: {lastname}, Год рождения: {year_of_birth}, '
                 f'Город проживания: {city}, email: {email}, Телефон: {telephone_number}')

person(name=input('Ваше имя: '),
       lastname=input('Ваша фамилия: '),
year_of_birth = input('Год рождения: '),
city = input('Город проживания: '),
email = input('Email: '),
telephone_number = input('Номер телефона: '))
