import numpy as np
N = int(input())
n2 = np.base_repr(N, 2)
print(n2.zfill(10))
