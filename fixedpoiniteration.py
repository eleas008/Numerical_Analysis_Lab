import math
def func(x):
    return x**3-x**2-1
def rootf(x):
    return (x**2+1)**(1/3)
def fixediteration(a,t):
    count=0
    condition=True
    while condition:
        A=rootf(a)
        a=A
        count+=1
        condition=abs(func(A))>t
    print("Number of count: ",count)
    print("The Root:","%.4f"%A)

a=float(input("Enter Guess: "))
t=float(input("Enter Tolerance: "))
fixediteration(a,t)