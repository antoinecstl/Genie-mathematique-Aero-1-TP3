# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:34:41 2021

Stockage
"""

import math as m

def f1(x):
    return x**4+3*x-9
def fd1(x):
    return 4*x**3+3

def f2(x):
    return 3*m.cos(x)-2-x
def fd2(x):
    return -3*m.sin(x)-1

def f3(x):
    return x*m.exp(x)-7
def fd3(x):
    return m.exp(x)+x*m.exp(x)

def f4(x):
    return m.exp(x)-x-10
def fd4(x):
    return m.exp(x)-1

def f5(x):
    return 2*m.tan(x)-x-5
def fd5(x):
    return (2/(m.cos(x))**2)-x

def f6(x):
    return m.exp(x)-x**2-3
def fd6(x):
    return m.exp(x)-2*x 

def f7(x):
    return 3*x+4*m.ln(x)-7
def fd7(x):
    return 3+(4/x) 

def f8(x):
    return x**4-2*x**2+4*x-17
def fd8(x):
    return 4*x**3-4*x+4
    
def f9(x):
    return m.exp(x)-2*m.sin(x)-7
def fd9(x):
    return m.exp(x)-2*m.cos(x)

def f10(x):
    return m.ln(x**2+4)*m.exp(x)-10
def fd10(x):
    return m.exp(x)*((2*x)/(x**2+4)+m.log(x**2+4))




















