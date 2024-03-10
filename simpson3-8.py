import math
def func(exp,x):
    f=lambda x: eval(exp)
    return f(x)

def simpsons(exp,a,b,n):
    h=(b-a)/n
    x=[a+h*i for i in range(n+1)]
    y=[func(exp,x[i]) for i in range(n+1)]
    result=y[0]+y[n]
    for i in range(1,n,3):
        result+=3*(y[i]+y[i+1])
    for i in range(3,n-2,3):
        result+=2*y[i]
    return result*3*h/8
        
     
exp=input("Enter Expression: ")
a=int(input("Lower limit: "))
b=int(input("Upper limit: "))
n=int(input("Number of Intervals: "))
result=simpsons(exp,a,b,n)
print ("Integration: %f"%result)