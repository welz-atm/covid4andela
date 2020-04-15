from datetime import time


def calculate_period(x):
    if x == 'weeks':
        return x * 7
    elif x == 'month':
        return x * 30
    else:
        return x


def currentlyinfected(x):
    return x * 10


def currently_infected(x):
    return x * 50


def infectionbyrequestedattime(x,y):
    factor = calculate_period(x) // 3
    return currentlyinfected(y) * 2 ** factor


def severecasesbyrequestedtime(x):
    return x * 0.15


def hospitalbedsperrequestedtime(x,y):
    return (x * 0.35) - y


def casesforicubyrequestedtime(x):
    return x * 0.05


def casesforventilatorsbyrequestedtime(x):
    return x * 0.02


def dollarsinflight(x,y):
    return (x * 0.65) * y * 30


