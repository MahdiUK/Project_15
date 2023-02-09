
a = float(input("Please Enter a: "))
b = float(input("Please Enter b: "))
c = float(input("Please Enter c: "))

if a > b:
    temp = a
    a = b
    b = temp

if b > c:
    temp = b
    b = c
    c = temp

if a > c:
    temp = a
    a = c
    c = temp
print ("Your sorted numbers: ", a,b,c)
