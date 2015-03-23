def inverse(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x
print("Calcula si los valores son: palindromos, non lychrel o candidato a lychrel")

numbers=[]
lychrel=[]

x=int(input("Dame el limite inferior de los numeros a tomar en cuenta: "))
x1=int(input("Dame el limite superior de los numeros a tomar en cuenta: "))

print ("El rango de números analizados va de",x,"a",x1)

for i in range(x1-x+1):
    numbers.append(x)
    x=x+1

a=0
b=0
ab=0
for i in numbers:
    y=inverse(i)
    if i==y:
        a=a+1
    else:
        z=i+y
        y1=inverse(z)
        for i1 in range(30):
            if z==y1:
                ab=ab+1
                break
            else:
                z=z+y1
                y1=inverse(z)
                if i1==29:
                    b=b+1
                    lychrel.append(i)
print("El numero de palindromos es: ",a)
print("El numero de non lychrel es: ",ab)
print("El numero de candidatos a lychrel es: ",b)
if b!= 0:
    print ("números Lychrel encontrados: ")
    print (lychrel)
