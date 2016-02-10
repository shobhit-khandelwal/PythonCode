import random
import math

def S(n,lam): 
    k=1
    t=0    
    for i in range(1,n):
        U=random.uniform(0,n)
        tk=t+(-(1/lam)*math.log(U))
        print tk
    return tk

print S(10,3)