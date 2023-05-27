import random
import numpy as np

a=1
zote=21
C_rate=int(input('Dime Crossover rate: '))
M_rate=int(input('Dime Mutation rate: '))
poblacion = np.zeros((100,20))
poblacion1= np.zeros((100,20))
fitnes=np.zeros(100)
for i in range(100):
  for j in range(20):
    ran=random.randint(0,1)
    if ran==0:
      poblacion[i,j]=int(0)
      poblacion1[i,j]=poblacion[i,j]
    if ran==1:
      poblacion[i,j]=1
      poblacion1[i,j]=poblacion[i,j]
###### sacar los 1 que hay por cada 1 de los 100
genfit=0
for i in range(100):
  totalf=0
  for j in range(20):
    if poblacion[i,j]==1:
      totalf=totalf+1
  fitnes[i]=totalf
  if totalf==20:
    a=0
    zote=i
  genfit=genfit+totalf
unos_poblacion=genfit
########
generacion=1
#####IMPRIME LA mATRIS
j=0
for i in range(100):
  print(i,"=i-",poblacion[i,j],poblacion[i,j+1],poblacion[i,j+2],poblacion[i,j+3],"-",poblacion[i,j+4],poblacion[i,j+5],poblacion[i,j+6],poblacion[i,j+7],"-",poblacion[i,j+8],poblacion[i,j+9],poblacion[i,j+10],poblacion[i,j+11],"-",poblacion[i,j+12],poblacion[i,j+13],poblacion[i,j+14],poblacion[i,j+15],"-",poblacion[i,j+16],poblacion[i,j+17],poblacion[i,j+18],poblacion[i,j+19],"fitness=",fitnes[i])
print("unos totales",genfit)
print("generacion=",generacion)
#######crossover
while(a!=0):
  generacion=generacion+1
  for i in range(100):
    pro_=random.randint(1,100)
    if C_rate>pro_:
      padre=0
      nemo=random.randint(1,genfit)
      while nemo>fitnes[j] and nemo<fitnes[j+1]:####validar que no se combine consigo mismo
        nemo=random.randint(1,genfit)
      for j in range(100):
        padre=padre+fitnes[j]
        if padre>nemo:
          abu=j
          break
      rango_20=random.randint(0,19)
      numero_de_cambios=0
      for j in range(20):
        if j>=rango_20:
          numero_de_cambios=numero_de_cambios+1
          cambio=poblacion[i,j]
          poblacion[i,j]=poblacion[abu,j]
          poblacion[abu,j]=cambio
#############

###############mutacion
  for i in range(100):
    pro_=random.randint(1,100)
    if M_rate>pro_:
      pro_=random.randint(0,19)
      if poblacion[i,pro_]==1:
        poblacion[i,pro_]=0
      else:
        poblacion[i,pro_]=1

########
  genfit=0
  for t in range(100):
    totalf=0
    for j in range(20):
      if poblacion[t,j]==1:
        totalf=totalf+1
    fitnes[t]=totalf
    if totalf==20:
      a=0
      zote=t
    genfit=genfit+totalf
  if a==0:
    break
########

###########
  j=0
  for i in range(100):
    print(i,"=i-",poblacion[i,j],poblacion[i,j+1],poblacion[i,j+2],poblacion[i,j+3],"-",poblacion[i,j+4],poblacion[i,j+5],poblacion[i,j+6],poblacion[i,j+7],"-",poblacion[i,j+8],poblacion[i,j+9],poblacion[i,j+10],poblacion[i,j+11],"-",poblacion[i,j+12],poblacion[i,j+13],poblacion[i,j+14],poblacion[i,j+15],"-",poblacion[i,j+16],poblacion[i,j+17],poblacion[i,j+18],poblacion[i,j+19],"fitness=",fitnes[i])
  print("unos totales",genfit)
  print("generacion=",generacion)
j=0
for i in range(100):
  print(i,"=i-",poblacion[i,j],poblacion[i,j+1],poblacion[i,j+2],poblacion[i,j+3],"-",poblacion[i,j+4],poblacion[i,j+5],poblacion[i,j+6],poblacion[i,j+7],"-",poblacion[i,j+8],poblacion[i,j+9],poblacion[i,j+10],poblacion[i,j+11],"-",poblacion[i,j+12],poblacion[i,j+13],poblacion[i,j+14],poblacion[i,j+15],"-",poblacion[i,j+16],poblacion[i,j+17],poblacion[i,j+18],poblacion[i,j+19],"fitness=",fitnes[i])
print("unos totales",genfit)
print("generacion=",generacion)  
print("zote=",zote)
########