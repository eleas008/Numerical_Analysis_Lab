import math
def func(exp,x):
    f=lambda x: eval(exp)
    return f(x)
def numerical_diff(a,h,method,exp):
    if method=="Forward":
        return (func(exp,a+h)-func(exp,a))/h
    elif method=="Backward":
        return (func(exp,a)-func(exp,a-h))/h
    elif method=="Central":
        return (func(exp,a+h)-func(exp,a-h))/(2*h)

exp=input("Enter Expression: ")
a=float(input("Find derivative at : "))
h=float(input("Difference: "))
method=input("Enter Method: ")
numerical_derivative=numerical_diff(a,h,method,exp)
print("Numerical derivatives: %f"%numerical_derivative)
