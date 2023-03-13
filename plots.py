from gen_testing_set import *

import matplotlib.pyplot as plt
import numpy as np
import os


l = 200
begin = -5
end = 5
x = [np.array([feature]) for feature in np.linspace(begin, end, l)]

expectedValue = 0
standardDeviation = 1

generators = [
    ("sin", SinTestingSet),
    ("csin", CSinTestingSet),
    ("noised sin", lambda x: AddNoise(SinTestingSet(x), expectedValue, standardDeviation)),
    ("noised csin", lambda x: AddNoise(CSinTestingSet(x), expectedValue, standardDeviation))
]

os.mkdir("images")

for generator in generators:
    plt.plot(x, generator[1](x))
    plt.title(generator[0])
    plt.grid(True)
    plt.savefig("images/{}".format(generator[0].replace(' ', '_')))
    plt.show()
