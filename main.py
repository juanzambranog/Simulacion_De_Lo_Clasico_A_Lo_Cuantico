import matplotlib.pyplot as plot
import numpy as np


def sis_prob(dinamica, estadoI, clicks):
    for i in range(clicks):
        estadoI = np.dot(dinamica, estadoI)
    return estadoI


def multipleSlit(dinamica, estadoI, clicks):
    for i in range(clicks):
        estadoI = np.dot(dinamica, estadoI)
    return estadoI


def multipleSlitCuantico(dinamica, estadoI, clicks):
    cop = dinamica[:]
    for i in range(clicks):
        dinamica = np.dot(dinamica, cop)

    for i in range(len(dinamica)):
        nueva = []
        for j in range(len(dinamica[i])):
            nueva.append([np.linalg.norm(dinamica[i][j]) ** 2, 0])
        dinamica[i] = nueva
    return dinamica


def exp(dinamica, estadoI, clicks):
    for i in range(clicks):
        if len(estadoI) == len(dinamica[0]):
            nueva = [False for i in range(len(dinamica))]
            for i in range(len(dinamica)):
                a = True
                for j in range(len(dinamica[i])):
                    a = dinamica[i][j] and estadoI[j]
                    nueva[i] = nueva[i] or a
            return nueva

def grafico(estadoI):
    data = len(estadoI)
    x = np.array([x for x in range(data)])
    y = np.array([round(estadoI[x][0] * 100, 2) for x in range(data)])

    plot.bar(x, y, color='r', align='center')
    plot.title('vector')
    plot.show()


