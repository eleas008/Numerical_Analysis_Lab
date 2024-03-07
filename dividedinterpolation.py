import math
def func(e,x):
    f=lambda x: eval(e)
    return f(x)

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
        y[j][i]=(y[j+1][i-1]-y[j][i-1])/(x[j+i]-x[j])

for i in range(n):
    print(x[i],end="\t")
    for j in range(n-i):
        print(y[i][j],end="\t")
    print(" ")

value=float(input("Enter an interpolated value: "))
sum=y[0][0]
product = 1
for i in range(1,n):
    product = product*(value-x[i-1])
    sum = sum + product*y[0][i]
print("The result is %.6f"%sum)
