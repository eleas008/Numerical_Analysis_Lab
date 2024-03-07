import math
def func(e,x):
    f=lambda x: eval(e)
    return f(x)

def prod(p,n):
    product=p
    for i in range(1,n):
        product*=(p-i)
    return product

e=input("Enter an Expression: ")
n=int(input("Enter the size of x array: "))
x=[]
y=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    x_val=float(input(f"Enter x[{i}]: "))
    x.append(x_val)
    y[i][0]=func(e,x_val)

for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]

for i in range(n):
    print(x[i],end="\t")
    for j in range(n-i):
        print(y[i][j],end="\t")
    print(" ")

value=float(input("Enter an interpolated value: "))
p=(value-x[0])/(x[1]-x[0])
sum=y[0][0]
for i in range(1,n):
    sum+=(prod(p,i)*y[0][i])/math.factorial(i)

print("The result is %.6f"%sum)
