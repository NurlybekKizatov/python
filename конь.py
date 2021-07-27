k1 = int(input())
k2 = int(input())
f1 = int(input())
f2 = int(input())

x = f1 - k1
y = f2 - k2 
if x<0 :
    x = -x 
if y<0 :
    y = -y
if (x == 2 and y == 1) or (x == 1 and y == 2) :
    print("yes")
else :
    print("no")
