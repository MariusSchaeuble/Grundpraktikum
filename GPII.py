
import numpy as np
import sympy as sym
from Helpers import identifier, roundUP
import math


def roundSci(messwert, fehler):
    if fehler == 0:
        print('Fehler von 0, macht keinen Sinn')
        return None
    fehlerStr = str(fehler)
    k = -127
    p = fehlerStr.find('.')
    if p != -1:
        for i in range(0, len(fehlerStr)):
            if fehlerStr[i] in ["3", "4", "5", "6", "7", "8", "9"]:
                if i < p:
                    k = i - p + 1
                else:
                    k = i - p
                break
            if fehlerStr[i] in ['1', '2']:
                if i+1 < p:
                    k = i - p + 2
                else:
                    k = i - p + 1
                    if k == 0:
                        k = 1
                break
        e = fehlerStr.find('e')
        if e != -1:
            k -= int(fehlerStr[e+1:len(fehlerStr)])
    else:
        #kein komma
        e = fehlerStr.find('e')
        if e == -1:
            for i in range(len(fehlerStr)):
                if fehlerStr[i] in ['3', '4', '5', '6', '7', '8', '9']:
                    k = i - len(fehlerStr) + 1
                    break
                if fehlerStr[i] in ['1', '2']:
                    k = i - len(fehlerStr) + 2
                    break
        else:
            for i in range(e):
                if fehlerStr[i] in ['3', '4 ', '5', '6', '7', '8', '9']:
                    k = i - e + 1
                    break
                if fehlerStr[i] in ['1', '2']:
                    k = i - e + 2
                    break
            k -= int(fehlerStr[e+1:len(fehlerStr)])
    #eigentliches runden, mit ermitteltem k
    fehler *= math.pow(10, k)
    fehler = roundUP(fehler)
    fehler /= math.pow(10, k)
    messwert *= math.pow(10, k)
    messwert = round(messwert)
    messwert /= math.pow(10, k)
    anzahlStellen = str(int(max([0, k])))
    fehlerFormat = "." + anzahlStellen + "f"
    fehler  = format(fehler, fehlerFormat)

    messwertFormat = "." + anzahlStellen + "f"
    messwert  = format(messwert, messwertFormat)
    return [messwert, fehler, k]


def latexTable(*spalten):
    shp = len(spalten)
    if shp == 0:
        print("Keine Matrix erhalten, len spalten = 0")
        return None
    maxIndex = 0
    for i in range(shp):
        if len(spalten[i]) > maxIndex:
            maxIndex = i

    maxLength = len(spalten[maxIndex])
    result = 'copy below' + '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \|/' + '\n' + '\n'
    result += r'\begin{table}[H]' + '\n'
    result += '\centering' + '\n'
    result += r'\label{LABEL}' + '\n'
    result += r'\caption{CAPTION}' + '\n'

    result += r'\begin{tabular}{|'
    for i in range(shp):
        result += r'c|'
    result += '}' + '\n' + '\hline' + '\n' + '\n'
    for i in range(shp - 1):
        result += 'Bezeichnung' + str(i+1) + ' & '
    result += 'Bezeichnung' + str(shp) + r'\\'
    result += '\n' + r'\hline' + '\n'
    for i in range(maxLength):
        result += '\n'
        for j in range(shp - 1):
            if i < len(spalten[j]):
                result += '$' + spalten[j][i] + '$' + ' & '
            else:
                result += '&'
        result += '$' + spalten[shp-1][i] + '$' + r'\\'

    result += '\n' + '\n' + '\hline'
    result += '\n' + r'\end{tabular}'
    result += '\n' + '\end{table}' + '\n' + '\n' + r'- - - - - - - - - - - - - - - - - - - - - - - /|' + r'\ '
    print(result)


def roundCol(vector, errorVector, unitString='', factor=0):
    if vector.size != errorVector.size or vector.size == 0 or errorVector.size == 0:
        print('Längen ungleich odewr Längen sind 0')
        return None
    length = len(vector)
    result = []
    for i in range(length):
        rounded = roundSci(vector[i], errorVector[i])
        if factor == 0:
            result.append('(' + rounded[0] + ' \pm ' + rounded[1] + ')' + '\,' + '\mathrm{' + unitString + '}')
        else:
            value = float(rounded[0])*math.pow(10, factor)
            valueErrorFormat = '.' + str(max([0, int(rounded[2]) - factor])) + 'f'
            value = format(value, valueErrorFormat)
            error = float(rounded[1])*math.pow(10, factor)
            error = format(error, valueErrorFormat)
            result.append('(' + value + ' \pm ' + error + ')' + '\,' + '\mathrm{' + unitString + '}')
    return result


def RC(vector, errorVector, unitString='', factor=0):
    return roundCol(vector, errorVector, unitString, factor)


def nameCol(n):
    result = []
    for i in range(n):
        result.append('N_{\mathrm{' + str(i) + '}}')
    return result


def indexCol(n):
    result = []
    for i in range(n):
        result.append(str(i))
    return result


def unitCol(vector, unitString='', factor=0):
    result = []
    for i in range(vector.size):
        result.append(str(vector[i]*math.pow(10, factor)) + '\,' + '\mathrm{' + unitString + '}')
    return result




