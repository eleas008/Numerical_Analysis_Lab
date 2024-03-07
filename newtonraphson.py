import math
def func(x):
    return x*math.sin(x)+math.cos(x)
def diff(x):
    return x*math.cos(x)
def newtonraphson(a,t):
    count=0
    condition=True
    while condition:
        if (diff(a)==0.0):
            print("Divide by Zero Error!")
            break
        A=a-func(a)/diff(a)
        a=A
        count+=1
        condition=abs(func(A))>t
    print("Number of count: ",count)
    print("The Root:","%.4f"%A)

a=float(input("Enter Guess: "))
t=float(input("Enter Tolerance: "))
newtonraphson(a,t)