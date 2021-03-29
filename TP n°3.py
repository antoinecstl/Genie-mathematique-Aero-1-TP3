# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:09:54 2021

@author: Toniocstl
"""
import TP3annexe as a
def Newton(f,fd,x0,epsilon,Nitermax):
    n=0
    xold = x0
    erreur = f(xold) - xold
    while abs(erreur)> epsilon and n<Nitermax:
        xnew = xold-(f(xold)/fd(xold))
        erreur = xnew - xold
        xold = xnew
        print(n)
        n+=1
    return xnew 

print('xnew=',Newton(a.f2, a.fd2, -5, 1e-10,5e4))
