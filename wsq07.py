print("Sum of numbers")
print("Este programa calcula la suma de un rango de numeros")
x=int(input("Dame un numero: "))
y=int(input("Dame otro numero: "))
z=0
for i in range(x,y,1):
    z += i
print(z)
