# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


# def power(a,b):
#     if b == 1:
#         return 1
#     else:

#         return a*power(a,b-1)

# print("Задача 26")
# n=-1
# while n<=0:
#     n = int(input("Введите число: "))
# m=-1
# while m<=0:
#     m = int(input("Введите степень,  в которую будем возводить: "))
# print(f"Ваше рузльтат {power(n,m)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# 2 2
#     4 



# def sum(a,b):
#     if b > 0 :
#         return 1 + sum(a,b-1)
#     else:
#         if a > 0:
#             return  1  + sum(a-1, 0)
            
#         else:
#             return 0
    
    

# print("Задача 28")
# n=-1
# while n<=0:
#     n = int(input("Введите число 1: "))
# m=-1
# while m<=0:
#     m = int(input("Введите число 2: "))
# print(f"Ваше рузльтат {sum(n,m)}")