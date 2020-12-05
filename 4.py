# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.Подсказка: попробуйте решить задачу двумя
# способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора
# **, предусматривающая использование цикла.


def my_func(x, y):
    if y >0 :
        y = -y
    return x**y
    # count = -1
    # while count > y:
    #     x *= x
    #     count -=1
    # return  1/x


print(my_func(2, -2))
