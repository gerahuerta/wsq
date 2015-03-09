#Gerardo Huerta Ruiz
#A01229724

def hacer_la_suma(x,y):
    answer= x+y
    return answer

def hacer_la_resta(x,y):
    answer= x-y
    return answer

def hacer_la_multiplicacion(x,y):
    answer= x*y
    return answer

def hacer_la_division(x,y):
    answer= x/y
    return answer
print("Este programa hace operaciones con dos integrales")
uno=int(input("Dame la primera integral "))
dos=int(input("Dame la segunda integral "))
print("los numeros que me diste son",uno,"y",dos)

la_suma= hacer_la_suma(uno,dos)
la_resta= hacer_la_resta(uno,dos)
la_multiplicacion= hacer_la_multiplicacion(uno,dos)
la_division= hacer_la_division(uno,dos)

print("la suma de los numero es: ",la_suma)
print("la resta de los numero es: ",la_resta)
print("la multiplicacion de los numero es: ",la_multiplicacion)
print("la division de los numero es: ",la_division)
