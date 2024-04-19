import matplotlib
import numpy as np
import sympy as sym
from Helpers import identifier, isCharacter
import math
from numpy import matrix, array
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, title
import scipy.optimize as opt
from GPII import *
from math import sqrt


plt.rcParams["text.usetex"] = True
tex_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 10,
    "font.size": 10,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8
}

plt.rcParams.update(tex_fonts)
plt.rc('text', usetex=True)







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

