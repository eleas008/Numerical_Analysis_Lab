import math
def func(e,x):
    f=lambda x: eval(e)
    return f(x)

def lagrange(x,y,value):
    result=0
    n=len(x)
    for i in range(n):
        term=y[i]
        for j in range(n):
            if(j!=i):
                term*=(value-x[j])/(x[i]-x[j])
        result+=term
    return result

e=input("Enter an Expression: ")
n=int(input("Enter the size of x array: "))
x=[]
y=[]

for i in range(n):
    x_val=float(input(f"Enter x[{i}]: "))
    x.append(x_val)
    y_val=func(e,x_val)
    y.append(y_val)

value=float(input("Enter an interpolated value: "))
ipvalue=lagrange(x,y,value)
print("Result: %f"%ipvalue)