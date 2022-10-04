list = list(map(int, input("Введите числа через пробел: \n").split())) 
def sum_odd_index(list):
    s = 0
    for i in range(len(list)):
       
        if i % 2 != 0:
            s += list[i]
            
    print(f"Сумма равна: {s}")
sum_odd_index(list)