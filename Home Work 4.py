# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастаниявсе те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# print("Задача 22")
# n=-1
# while n<=0:
#     n = int(input("Введите количтесво чисел в 1 наборе: "))
# m=-1
# while m<=0:
#     m = int(input("Введите количтесво чисел во 2 наборе: "))
# string_digit = input("Введите строку с цифрами через пробел: ")
# arr1 = list(map(int, string_digit.split(' ')))
# string_digit = input("Введите строку с цифрами через пробел: ")
# arr2 = list(map(int, string_digit.split(' ')))
# arr1.sort()
# arr2.sort()
# m1 = set(arr1)
# m2 = set(arr2)
# sets_final = set()
# sets_final = m1.intersection(m2)
# print(sets_final)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданнойво входном файле грядки.


# print("Задача 24")
# n=-1
# while n<=0:
#     n = int(input("Введите кол-во кустов: "))
# arr = list()
# for i in range (n):
#     s = int(input(f"Введите кол-во ягод на {i}-ом кусте: "))
#     arr.append(s)
# count_list = list()
# for i in range( len(arr)-1):
#     count_list.append(arr[i]+arr[i-1]+arr[i+1])
# count_list.append(arr[-1]+arr[0]+arr[-2])
# print(max(count_list))