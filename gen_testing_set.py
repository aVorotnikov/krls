import numpy as np


def SinTestingSet(x):
    return np.array([np.sin(feature[0]) for feature in x])


def CSinTestingSet(x):
    return np.array([np.sinc(feature[0]) for feature in x])


def AddNoise(y : np.array, expectedValue = 0, standardDeviation = 1):
    return np.array([val + np.random.normal(expectedValue, standardDeviation) for val in y])
