def sqrt(a):
    if a==0:
        return a
    elif a<0:
        return ("Error: La raíz cuadrada de un número negativo es un número imaginario")
    else:
        n=0
        i=0
        while n<a:
            n=i**2
            i=i+1

        if n==a:
            return (i-1)

        else:
            g=(i-1)
            ng=((a/g)+g)/2
            while (ng != g):
                g=ng
                ng=((a/g)+g)/2
            return ng

r='y'
while r=='y' or r=='Y':
    while True:
        try:
            x=float(input("Por favor, introduzca un número para aplicar la raíz cuadrada: "))
            break
        except ValueError:
            print ("Este no es un numero porfavor intente de nuevo")

    print (sqrt(x))
    r=input("¿Quieres probar cualquier otro número? (S / n)")
