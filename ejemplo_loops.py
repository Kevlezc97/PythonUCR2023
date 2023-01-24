""" CICLOS , BUCLES o LOOPS
#Imprimir todos los números del 0 al 6 """
i = 0
while i < 6:
    i += 1
    print (i)
#Imprimir todos los números del 0 al 6, saltandose el 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)
#Imprimir todos los números del 0 al 6, saltandose el 3
i = 1
while i < 6:
    print (i)
    i += 1
else:
    print("Ya no se cumple la condición")

#FOR

#for i in range(6):
 #   print("seis")

for i in range(0,6,2):
    print("seis")


