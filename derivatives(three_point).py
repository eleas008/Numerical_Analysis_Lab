import math
def func(e,x):
    f=lambda x: eval(e)
    return f(x)
e=input("Enter Expression: ")
a=float(input("Enter a value: "))
h=float(input("Enter difference: "))
diff_a=((-3*func(e,a))+(4*func(e,a+h))-(func(e,a+2*h)))/(2*h)
print("The result three point endpoint: %.6f"%diff_a)
dif_a=(func(e,a+h)-func(e,a-h))/(2*h)
print("The result of three point midpoint: %.6f"%dif_a)