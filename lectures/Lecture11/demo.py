import numpy as np
from scipy import linalg

from ica import fastica

import line_profiler
profile = line_profiler.LineProfiler()


@profile
def test():
    data = np.random.random((5000, 100))
    u, s, v = linalg.svd(data)
    pca = np.dot(u[:, :10].T, data)
    results = fastica(pca.T, whiten=False)

if __name__ == '__main__':
    test()