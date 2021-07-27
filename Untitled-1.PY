a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = input("Что будем делать?")

z = a + b 
x = a - b 
y = a / b 
w = a * b 

if c in '+'  :
    print ("Результат" + " " + str(z))
if c in '-'  :
    print ("Результат" + " " + str(x))

if c in '/'  :
    print ("Результат" + " " + str(y))

if c in '*'  :
    print ("Результат" + " " + str(w))
input()