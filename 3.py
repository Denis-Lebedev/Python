# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

user_mounth = int(input("Введите номер месяца"))
month_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осен', 'Зима']
if 0 >= user_mounth > 12:
    print('Неверно укзан месяц')
else:
    print(f'Вы указали {user_mounth}й месяц это {month_list[user_mounth - 1]}')

month_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
              10: "Осень", 11: "Осень", 12: "Зима"}

print(f'Вы указали {user_mounth}й месяц это {month_dict[user_mounth]}')