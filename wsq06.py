print("Pick a number")
print("Este programa genera un numero random y pregunta al usuario adivinarlo")
import random
rndm=random.randint(0,100)
print("El numero es:  ",rndm)
tries=1
num=int(input("Escoje un numero del 1 al 100: "))
while(num!=rndm):
    if(num>rndm):
        print("Tu numero es muy grande")
    elif(num<rndm):
        print("tu numero es muy pequeño")
    num=int(input("Escoje un numero del 1 al 100: "))
    tries=tries+1
print("Felicidades tu adivinaste el numero {} , en {} oportunidades.".format(num,tries))
