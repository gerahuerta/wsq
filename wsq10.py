import statistics

def totalsum (m):
    total=0
    for indice in range(len(m)):
        total = total + m[indice]
    return total

def average (m):
    av = mitotal / 10.0
    return av

def standevi (m):
    sd = statistics.stdev(l)
    return sd

l=[]
x = 0

while (x < 10):
    x = x + 1
    n = float(input("Dame un numero: "))
    l.append(n)
    mitotal = totalsum(l)
    promedio = average(l)
devi = standevi(l)

print("no mas valores.")
print("totalsuma: ", mitotal)
print("average: ", promedio)
print("Desviacion estandar: ", devi)
