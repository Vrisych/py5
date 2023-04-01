#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def step (osn, st, mn=1):
    if st>1:
        mn*=osn
        st-=1
        return step(osn, st, mn)
    else: 
        return mn*osn

A=int(input('Введите число: '))
B=int(input('Введите степень: '))
print(f'Число {A} в степени {B} равно {step(A,B)}')