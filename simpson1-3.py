import math
def func(exp,x):
    f=lambda x: eval(exp)
    return f(x)

def simpsons(exp,a,b,n):
    h=(b-a)/n
    x=[a+h*i for i in range(n+1)]
    y=[func(exp,x[i]) for i in range(n+1)]
    result=y[0]+y[n]
    for i in range(1,n,2):
        result+=4*y[i]
    for i in range(2,n-1,2):
        result+=2*y[i]
    return result*(h/3)
     
exp=input("Enter Expression: ")
a=int(input("Lower limit: "))
b=int(input("Upper limit: "))
n=int(input("Number of division: "))
result=simpsons(exp,a,b,n)
print ("Integration: %f"%result)