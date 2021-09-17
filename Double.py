import math
x = float(input("Введите x"))
y = float(input("Введите y"))

if x>0 and y>0:
    print("Точка принадлежит 1 четверти")
elif x<0 and y>0:
    print("Точка принадлежит 2 четверти")
elif x < 0 and y < 0:
    print("Точка принадлежит 3 четверти")
elif x>0 and y<0:
    print("Точка принадлежит 4 четверти")
elif y==0 and x!=0:
    print("Точка лежит на оси ОХ")
elif x==0 and y!=0:
    print("Точка лежит на оси ОУ")
else:
    print("Данная точка - начало координат")

