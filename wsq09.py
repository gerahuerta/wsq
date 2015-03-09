def factorial(n):
    a= n
    b= 1
    while (a>1):
        b=b*a
        a=a-1
    return b

x="s"
while (x=="s"):
    n= int(input("Pon un entero"))
    h= factorial(n)
    if (n<0):
        print("Porfavor poner un numero positivo")
    else:
        print("el factorial de ",n," es ",h)
        x=input("Quieres intentar con un numero diferente? s/n ")
