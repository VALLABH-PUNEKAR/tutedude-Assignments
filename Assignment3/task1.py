
def factorial(a):
    if(a<2):
        return 1
    return a*factorial(a-1)
n=int(input("Enter a number:"))
result=factorial(n)
print("factorial of ",n," is ",result)