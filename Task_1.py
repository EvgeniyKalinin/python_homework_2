# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
from random import randint

n = int(input("Введите количество монет -->   "))
numbers = []


for i in range(n):
    numbers.append(randint(0, 1))
print(numbers)
count_0 = 0
count_1 = 0


for i in range(n):
    if numbers[i] == 1:
        count_1 +=  1
    else:
        count_0 += 1


if count_1 < count_0:
    print(f"Наименьшее число переворотов -->   {count_1} ")

else:
    print(f"Наименьшее число переворотов -->   {count_0} ")