...
200011735 Daniel Evanio 
200011514 Thais Ferreira
...

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv(r"C:\Users\daniel\Desktop\Unisal\3S\PP-seg\a12\GasPreco.csv")
plt.plot(gas.Year, gas.Canada)
plt.plot(gas.Year, gas.USA)
plt.plot(gas.Year, gas.Mexico)
plt.show()