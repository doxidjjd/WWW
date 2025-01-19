#задача 1
num_1=int(input("Введи перше число: "))
num_2=int(input("Введи друге число: "))
num_3=int(input("Введи третє число: "))
U=input("Введи знак дії: + чи - ")
if U=="+":
   print( num_1+num_2+num_3)
elif U=="-":
    print(num_1-num_2-num_3)
else:
    print("Ти ввів неправильний знак!")
# Ввод данных
a=int(input("Введи перше число: "))
b=int(input("Введи друге число: "))
c=int(input("Введи третє число: "))
U = input("Введи команду Max, min, average:  ") 

#задача 2
if U == "Max":
    if a >= b and a >= c:  
        print("Max:", a)
    elif b >= a and b >= c:  
        print("Max:", b)
    else:  
        print("Max:", c)
elif U == "min":
    if a <= b and a <= c: 
        print("Min:", a)
    elif b <= a and b <= c:  
        print("Min:", b)
    else:  
        print("Min:", c)
elif U == "average":
    average = (a + b + c) / 3 
    print("Average", average)
else:
    print("Ти ввів неправильний знак!")
#задача 3
m=float(input("Введи метри для конвертації в іншу одиницю вимірювання: "))
c=float(input("\tВведи: \n1 для милей \n2 для дюйми \n3 для ярди \n4 для кілометрів \n5 для сантимертрів \n6 для міліметрів \n7 для мікрометр \n8 для нанометр \n9 для пікометр \n10 для фемтометр \n11 для морська миля \n12 для світового року \n13 для астрономічна одиниця \n14 для кроків людини ")) 
if c==1:
  print("Милі:",m/1609.34)  
elif c==2:
   print("Дюйми:",m*39.3701)  
elif c==3:
   print("Ярди:",m*1.09361)
elif c==4:
   print("Кілометри:",m/1000)
elif c==5:
   print("Сантиметри:",m*100)
elif c==6:
   print("Міліметри:",m*1000)
elif c==7:
   print("Мікрометри:",m*1000000)
elif c==8:
   print("Нанометри:",m*100_000_000_000) #_-щоб нулі не згубити
elif c==9:
   print("Пікометри:",m*1_000_000_000_000)              
elif c==10:
   print("Фемтометри:",m*1_000_000_000_000_000)
elif c==11:
   print("Морська миля:",m/1852) 
elif c==12:
   print("Світовий рік:",m*1.057e-16) 
elif c==13:
   print("Астрономічна одиниця:",m*6.68459e-12) 
elif c==14:
   print("Кроків людини:",m/0.762)
else:
   print("Неправильний вибір!")            
