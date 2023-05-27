import os

xl=[]
yl=[]
b=[0]
xy=0
x=0
y=0
x2=0
n=0

n=int(input('Dime otra cantidad a registrar:'))

for i in range (n):
    print("R:",i+1)
    b[0]=int(input('Dime X:'))
    xl=xl+b
    b[0]=int(input('Dime Y:'))
    yl=yl+b

for i in range (n):
    xy=xy+xl[i]*yl[i]
    x=x+xl[i]
    y=y+yl[i]
    x2=x2+xl[i]*xl[i]

m=(n*xy-(x*y))/(n*x2-x*x)
inter=(y-m*x)/n
b=int(input('El numero a predecir:'))
print("prediccion es:",m*b+inter)