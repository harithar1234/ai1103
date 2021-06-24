

import numpy as np
nX=2
nY=20
nF=pow(nY,nX)
print("Number of functions from X to Y :",nF)

def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
#let O be set containing one-to-one functions from X to Y 

nO=factorial(nY)//factorial(nY-nX)

print("Number of one-to-one functions from X to Y :",nO)

#Pr(f)- the  probability  of  randomlychosen function f from F being one to one 

Prob_f=nO/nF

print("the  probability  of  randomly chosen function f from F being one to one is ",Prob_f)