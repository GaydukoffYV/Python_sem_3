# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
def dec_to_bin(n):
    if(n > 1):
        dec_to_bin(n//2)
    print(n%2,end='')    
if __name__=='__main__':
    dec_to_bin(n)
    print("\n")    