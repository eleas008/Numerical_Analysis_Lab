import math
def func(exp,x):
    f= lambda x: eval(exp)
    return f(x)
def falseposition(a,b,exp,t):
    if(func(exp,b)*func(exp,a)>=0):
        print("You've not assumed right a and b \n")
        return
    c=a
    count=0
    while True:
        c = (a * func(exp, b) - b * func(exp, a)) / (func(exp, b) - func(exp, a))
        count += 1
        
        if abs(func(exp, c)) < t or abs(b - a) < t:
            break
        elif func(exp, a) * func(exp, c) < 0:
            b = c
        elif func(exp, b) * func(exp, c) < 0:
            a = c
    print("Number of iteration: ",count)
    print("The root: ","%.4f"%c)

exp=input("Enter Expression: ")  
a=float(input("Enter a: "))
b=float(input("Enter b: "))
t=float(input("Enter Tollerence: "))
falseposition(a,b,exp,t)