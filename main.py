from scipy.integrate import quad, dblquad, tplquad
import scipy.special as special
import numpy as np
from numpy import *

def main():
    menu_choice = menu()
    if menu_choice == '1':
        result = Single_Integration()
    elif menu_choice == '2':
        result = Double_Integration()
    elif menu_choice == '3':
        result = Triple_Integration()

def menu():
    print('This is the Integral Solver over a general area')
    print('To see a list of mathematic functions go to functions.txt')
    print('Built-in functions:')
    print('+, -, *, /, **(exponent)')
    print('PINF (positive infinity), NINF (negative infinity)')
    print('pi, e constants.')
    print('')
    print('[1] Single Integration')
    print('[2] Double Intergration')
    print('[3] Triple Integration')
    return input('Please choose a type of Integration: ')

def Single_Integration():
    expression = input('Please enter the expression in terms of x: ')
    function = lambda x: eval(expression)
    low = eval(input('Please enter the outside lower limit: '))
    high = eval(input('Please enter the outside upper limit: '))
    result = quad(function, low, high)
    print(result)
    return result

def Double_Integration():
    expression = input('Please enter the expression in terms of x and y: ')
    order = input('Please enter the order of the integral variable from the inside out. Ex: yx or xy: ')
    if order=='yx':
        function = lambda y, x: eval(expression)
    elif order=='xy':
        function = lambda x, y: eval(expression)
    outlow = eval(input('Please enter the outside lower limit: '))
    outhigh = eval(input('Please enter the outside upper limit: '))
    low_expression = input('Please enter the inside lower limit: ')
    if order=='yx':
        inlow = lambda x: eval(low_expression)
    elif order=='xy':
        inlow = lambda y: eval(low_expression)
    high_expression = input('Please enter the inside upper limit: ')
    if order=='yx':
        inhigh = lambda x: eval(high_expression)
    elif order=='xy':
        inhigh = lambda y: eval(high_expression)
    result = dblquad(function, outlow, outhigh, inlow, inhigh)
    print(result)
    return result

def Triple_Integration():
    expression = input('Please enter the expression in terms of x, y, and z: ')
    order = input('Please enter the order of the integral variable from the inside out. Ex: zyx, zxy, xzy, etc.: ')
    if order=='zyx':
        function = lambda z, y, x: eval(expression)
    elif order=='zxy':
        function = lambda z, x, y: eval(expression)
    elif order=='yzx':
        function = lambda y, z, x: eval(expression)
    elif order=='yxz':
        function = lambda y, x, z: eval(expression)
    elif order=='xzy':
        function = lambda x, z, y: eval(expression)
    elif order=='xyz':
        function = lambda x, y, z: eval(expression)
    outlow = eval(input('Please enter the outside lower limit: '))
    outhigh = eval(input('Please enter the outside upper limit: '))
    low_expression1 = input('Please enter the middle lower limit: ')
    if order[2] == 'x':
        midlow = lambda x: eval(low_expression1)
    elif order[2] == 'y':
        midlow = lambda y: eval(low_expression1)
    elif order[2] == 'z':
        midlow = lambda z: eval(low_expression1)
    high_expression1 = input('Please enter the middle upper limit: ')
    if order[2] == 'x':
        midhigh = lambda x: eval(high_expression1)
    elif order[2] == 'y':
        midhigh = lambda y: eval(high_expression1)
    elif order[2] == 'z':
        midhigh = lambda z: eval(high_expression1)
    low_expression2 = input('Please enter the inside lower limit: ')
    if order=='zyx':
        inlow = lambda x, y: eval(low_expression2)
    elif order=='zxy':
        inlow = lambda y, x: eval(low_expression2)
    elif order=='yzx':
        inlow = lambda x, z: eval(low_expression2)
    elif order=='yxz':
        inlow = lambda z, x: eval(low_expression2)
    elif order=='xzy':
        inlow = lambda y, z: eval(low_expression2)
    elif order=='xyz':
        inlow = lambda z, y: eval(low_expression2)
    high_expression2 = input('Please enter the inside upper limit: ')
    if order=='zyx':
        inhigh = lambda x, y: eval(high_expression2)
    elif order=='zxy':
        inhigh = lambda y, x: eval(high_expression2)
    elif order=='yzx':
        inhigh = lambda x, z: eval(high_expression2)
    elif order=='yxz':
        inhigh = lambda z, x: eval(high_expression2)
    elif order=='xzy':
        inhigh = lambda y, z: eval(high_expression2)
    elif order=='xyz':
        inhigh = lambda z, y: eval(high_expression2)
    result = tplquad(function, outlow, outhigh, midlow, midhigh, inlow, inhigh)
    print(result)
    return result

main()