import math
def func(exp,x):
    f= lambda x: eval(exp)
    return f(x)

def bisection(a,b,exp,t):
    if(func(exp,b)*func(exp,a)>=0):
        print("You've not assumed right a and b \n")
        return
    c=a
    count=0
    print("count        a           b             c              f(c)")
    while(b-a>=t):
        c=(a+b)/2
        print("%d        %.4f          %.4f          %.4f          %.4f"%(count,a,b,c,func(exp,c)))
        count+=1
        if(func(exp,c)==0.0):
            break
        else:
            if(func(exp,a)*func(exp,c)<0):
                b=c
            elif(func(exp,b)*func(exp,c)<0):
                a=c
    print("Number of iteration: ",count)
    print("The root: ","%.4f"%c)

exp=input("Enter Expression: ")
a=float(input("Enter a: "))
b=float(input("Enter b: "))
t=float(input("Enter Tollerence: "))
bisection(a,b,exp,t)
