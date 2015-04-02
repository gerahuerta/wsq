def euclides(num1,num2):
    if(num1==num2):
        ans=num1
    elif(num1>num2):
        ans=euclides((num1-num2),num2)
    else:
        ans=(num1,(num2-num1))
    return ans
print("The greatest common divisor")
num1=int(input("Dame un numero"))
num2=int(input("Dame otro numero"))
gcd=euclides(num1,num2)
print("The greatest common divisor es",gcd)
