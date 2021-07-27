s1 = int(input())
s2 = int(input())
f1 = int(input())
f2= int(input())
x = s1 - f1 
y = s2 - f2
if x<0:
    x = -x
if y <0:
    y = -y
if x == y :
    print("Слон бьет фигуру")
else :
    print("Слон не бьет фигуру")