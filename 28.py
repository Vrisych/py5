#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(sum1, sum2):
    if sum2==0:
        return sum1
    else:
        sum1+=1
        sum2-=1
        return sum(sum1,sum2)

a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
print(f'Сумма чисел {a} и {b} равна {sum(a, b)}')