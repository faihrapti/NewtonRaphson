from math import *

def newton_raphson(F,f,a,M,acc,digits):
    n=0
    while n<M and abs(F(a))>acc and abs(f(a))>0:
        print ("Checking if root is:",a)
        a=a-F(a)/f(a)
        n+=1
    print("The final estimate of the root is ",round(a,digits))


""" Uncomment to test
newton_raphson(lambda x:2-sin(x)+x**5,lambda x:-cos(x)+5*x**4,0,100,0.0001,4)"
"""