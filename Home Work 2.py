Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

print("Задача 10")
n = -1
while n<=0:
    n = int(input("Введите колличество монет > 0: "))
varios = []
print("Если монета лежит орлом введите 1, если решкой - 0")
for i in range(n):
    varios.append(int(input()))
if varios.count(1) > varios.count(0):
    print(f"Минимальное колличество монет {varios.count(0)}")
else:
    print(f"Минимальное колличество монет {varios.count(1)}")


Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

print("Задача 12")
summa = int(input("Сумма чисел: "))
multiplai = int(input("Произведение чисел: "))
for i in range(summa):
    for j in range(multiplai):
        if i+j == summa and i*j == multiplai:
            print (f"Ваши загаданные числа: {i} и {j}")
            break

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print("Задача 14")
n = int(input("Введите число: "))
k = 1
print(f"Все степени двойки меньше {n}")
while 2**k <=n:
    print(2**k)
    k +=1
