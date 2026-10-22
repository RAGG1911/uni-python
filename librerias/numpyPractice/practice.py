import numpy as np

temp = np.array([[22.5, 23.0, 21.5], [20.0, 24.5, 22.0], [19.5, 22.0, 23.5]])

promFila= np.mean(temp, axis=1)
promColumna= np.mean(temp, axis=0)
