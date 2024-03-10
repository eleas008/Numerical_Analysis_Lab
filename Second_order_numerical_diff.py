import math
def func(exp,x):
    f=lambda x: eval(exp)
    return f(x)

def numerical_diff2(a,h,exp):
    return (func(exp,a+h)-2*func(exp,a)+func(exp,a-h))/(h**2)

exp=input("Enter Expression: ")
a=float(input("Find derivative at : "))
h=float(input("Difference: "))
try:
   numerical_Second_derivative=numerical_diff2(a,h,exp)
   print("Numerical Second derivatives: %f"%numerical_Second_derivative)
except Exception as e:
    print("Error: ",e)
