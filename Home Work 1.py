# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# print("Задача 2")
# a = input("Введите число :")
# print(f"Сумма = {sum(list(map(int,a)))}")





# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Из условий олучается формула S = 6x

# s = int(input("Введит число: "))
# if s%6 == 0:
#     print(f"Ответ: Петя - {int(s/6)} Катя - {int(s/6*4)} Серёжа - {int(s/6)}")
# else:
#     print("Ответ: Нет целочисленных решений!!!")





# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

# print("Задача 6")
# digit = input("Введите число: ")
# if len(digit) != 6:
#     print ("Введли не верное знаечение!")
# else:
#     array = list(map(int,digit))
#     if sum(array[0:3]) == sum(array[3:6]):
#         print("Yes")
#     else:
#         print("No")






# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

# print("Задача 8")
# n = int(input("Введите значение n: "))
# m = int(input("Введите значение m: "))              
# k = int(input("Введите значение k: "))
# print("YES" if k%m == 0 or k%n == 0 else "No")                                    