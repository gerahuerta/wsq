print("temperatura")
f=int(input("Dame la temperatura en fahrenheit  "))
c=int(5*(f-32)/9)
sentence="Una temperatura en {} fagrenheit es {} celsius.".format(f,c)
print(sentence)
if(c>=100):
    print("Water boils")
else:(c<100)
print("Water does not boil")
