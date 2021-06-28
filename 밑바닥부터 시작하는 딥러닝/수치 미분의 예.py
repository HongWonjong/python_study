import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 10e-4
    return (f(x+h) - f(x-h)) / 2*h

def function_1(x):
    return 0.01*x**2 + 0.1*x

