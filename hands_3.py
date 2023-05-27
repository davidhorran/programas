import os
xl=[]
yl=[]
b=[0]
xy=0
x=0
y=0
x2=0
x3=0
x4=0
yx2=0
n=0

n=int(input('Dime otra cantidad a registrar:'))

for i in range (n):
    print("R:",i+1)
    b[0]=float(input('Dime X:'))
    xl=xl+b
    b[0]=float(input('Dime Y:'))
    yl=yl+b

for i in range (n):
    x=x+xl[i]
    x2=x2+xl[i]*xl[i]
    x3=x3+xl[i]*xl[i]*xl[i]
    x4=x4+xl[i]*xl[i]*xl[i]*xl[i]
    y=y+yl[i]
    xy=xy+xl[i]*yl[i]
    yx2=yx2+yl[i]*xl[i]*xl[i]
ax1=n
ax2=x
ax3=x2
ay1=x
ay2=x2
ay3=x3
az1=x2
az2=x3
az3=x4
d0=y
d1=xy
d2=yx2

#"""cramer"""""

De=((ax1)*(ay2)*(az3)+(ax2)*(ay3)*(az1)+(ax3)*(ay1)*(az2))-((az1)*(ay2)*(ax3)+(az2)*(ay3)*(ax1)+(az3)*(ay1)*(ax2))
Dx=(d0*ay2*az3+ay1*az2*d2+az1*d1*ay3)-(az1*ay2*d2+d0*az2*ay3+ay1*d1*az3)
Dy=(ax1*d1*az3+ax2*d2*az1+ax3*d0*az2)-(az1*d1*ax3+az2*d2*ax1+az3*d0*ax2)
Dz=(ax1*ay2*d2+ax2*ay3*d0+ax3*ay1*d1)-(d0*ay2*ax3+d1*ay3*ax1+d2*ay1*ax2)
rx=Dx/De
ry=Dy/De
rz=Dz/De
for i in range (n):
    sse=(yl[i]-rx*xl[i]*xl[i]-ry*xl[i]-rz)*(yl[i]-rx*xl[i]*xl[i]-ry*xl[i]-rz)
    sst=(yl[i]-yl[4])*(yl[i]-yl[4])
print("R cuadrada:",1-(sse/sst))
print("A:",rx)
print("B:",ry)
print("C:",rz)
print("DE:",De)
print("Dx:",Dx)
print("Dy:",Dy)
print("Dz:",Dz)
print("x:",x)
print("y:",y)
print("x2:",x2)
print("x3:",x3)
print("x4:",x4)
print("yx:",xy)
print("yx2:",yx2)

