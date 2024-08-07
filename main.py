import matplotlib
import numpy
import numpy as np
import sympy as sym
from Helpers import identifier, isCharacter
import math
from numpy import matrix, array, mean, std, max, linspace, ones, sin, cos, tan, arctan, pi, sqrt, exp, arcsin, arccos, arctan2, sinh, cosh, zeros, log, diag, linspace, arange
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, title, savefig, errorbar, grid
import scipy.optimize as opt
from GPII import *
from math import sqrt
pi = math.pi
import scipy


matplotlib.rc('xtick', labelsize=20)
matplotlib.rc('ytick', labelsize=20)







def gauss(term):
    ids = identifier(term)
    symbols = []
    for str1 in ids:
        symbols.append(sym.sympify(str1))
    termSymbol = sym.sympify(term)
    values = []
    for ident in ids:
        exec("values.append(" + ident + ")")

    derivatives = []
    i = 0
    while i < len(symbols):
        r = sym.diff(termSymbol, symbols[i])
        j = 0
        while j < len(symbols):
            # exec('r.evalf(subs={symbols[j]: ' + values[j] + '})')
            r = r.evalf(subs={symbols[j]: values[j]})
            j += 1
        derivatives.append(r.evalf())
        i += 1
    i = 0
    while i < len(derivatives):
        exec("derivatives[i] *= sigma_" + ids[i])
        i = i + 1
    res = 0
    for z in derivatives:
        res += z ** 2
    return math.sqrt(res)

def gaussVec(term):
    ids = identifier(term)
    arrays = []
    for i in range(len(ids)):
        if isinstance(eval(ids[i]), np.ndarray):
            arrays.append(ids[i])
    arrayLength = len(eval(arrays[0]))
    symbols = []
    for str1 in ids:
        symbols.append(sym.sympify(str1))
    termSymbol = sym.sympify(term)
    res = []
    for k in range(arrayLength):
        values = []
        for ident in ids:
            if ident in arrays:
                exec("values.append(" + ident + "[k]" + ")")
            else:
                exec("values.append(" + ident + ")")
        derivatives = []
        i = 0
        while i < len(symbols):
            r = sym.diff(termSymbol, symbols[i])
            j = 0
            while j < len(symbols):
                r = r.evalf(subs={symbols[j]: values[j]})
                j += 1
            derivatives.append(r.evalf())
            i += 1
        i = 0
        sigmaArrays = []
        for t in range(len(ids)):
            if isinstance(eval("sigma_" + ids[t]), np.ndarray):
                sigmaArrays.append(ids[t])
        while i < len(derivatives):
            if ids[i] in sigmaArrays:
                exec("derivatives[i] *= sigma_" + ids[i] + "[k]")
            else:
                exec("derivatives[i] *= sigma_" + ids[i])
            i = i + 1
        resj = 0
        for z in derivatives:
            resj += z ** 2
        res.append(sqrt(resj))
    return array(res)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



a = np.matrix([1, 2, 3, 4])
b = a.size

print(identifier("aa*b^2 + 2cos(x) + cos(y) + cos(  exp(aze81^2s) + exp(aze82) + exp( + aa + b"))
print(identifier("a"))
print(isCharacter("1"))

x1 = sym.sympify('x')
y = sym.sympify('y')
#expr = sym.symbols('y')
expr = sym.sympify("log(sqrt(cos(2*x*y)))")

z = expr.evalf(subs={x1: 2.4, y: 1.1})

a = 5
b = 10
sigma_a = 4
sigma_b = 8
sigma_pi = 0



g = a*b
sigma_g = gauss("a*b*cos(a)")


pi = math.pi


roundSci(1, 1)



vec1_m = array([1, 2, 3, 4, 5, 6])
sigma_vec1 = array([2, 3, 4, 5, 6, 7])
vec2_m = np.zeros(6)
sigma_vec2_m = np.zeros(6)

for v in range(6):
    vec2_m[v] = vec1_m[v] * a
    temp = vec1_m[v]
    sigma_temp = sigma_vec1[v]
    sigma_vec2_m[v] = gauss("temp*a")

plot(vec1_m, vec2_m, 'x', label = "vec2")
xlabel('$vec_1$')
ylabel('vec2')
legend()
#show()


def linear(x, a, b):
    return a * x**2 + b


xdata = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
ydata = array([1, 8, 3, 3, 4, 5, 7, 8, 16])
plot(xdata, ydata, 'x', label="sigma_vec2")
optimizedParameters, s = opt.curve_fit(linear, xdata, ydata)
plt.plot(xdata, linear(xdata, *optimizedParameters), label="fit")
a_std, b_std = np.sqrt(np.diag(s))

plt.rcParams['text.latex.preamble'] = r"\usepackage{amsmath}"

plt.title(r"$\alpha$", fontsize=25)
plt.xlabel(r"$\alpha$", fontsize=25)

show()


arr1 = array([1, 2, 3, 4])
arr2 = array([1, 2, 3, 4])

liste1 = ['1', '2', '3', '4']
liste2 = ['5', '6', '7', '8', '9']


#tabelle = latexTable(liste1, liste2)

rounded = RC(100e10*arr1, 50.3e5*arr2, factor=-7)

latexTable(indexCol(4), rounded, unitCol(arr1, 'mV'), unitCol(arr2), nameCol(4))

matrix1 = matrix("""
1 2 3;
4 5 6;
7 8 9
""")

gr1 = 1
gr2 = 1
sigma_gr1 = 1
sigma_gr2 = 1
fort = gr1 + gr2
sigma_fort = gauss("gr1^2 + exp(cos(gr2))")

latexTable(RC(2, 1))
RCP(2, 1)
