from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, title
from numpy import array
import matplotlib.pyplot as plt

xdata = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
ydata = array([1, 8, 3, 3, 4, 5, 7, 8, 16])
plot(xdata, ydata, 'x')

plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
plt.title('$lpha_1$')
show()

