import numpy as np
from scipy import stats

class Resolver:
    def __init__(self, xs):
        self.xs = np.sort(np.array(xs))
        self.absolute_frequencies = self._set_absolute_frequencies()
        self.relative_frequencies = stats.relfreq(self.xs, numbins=len(self.xs) - 1)
        self.cumulative_frequencies = np.array([])
    
    def get_absolute_frequencies(self):
        return self.absolute_frequencies
    
    def get_relative_frequencies(self):
        return np.trim_zeros(self.relative_frequencies[0])
    
    def _set_absolute_frequencies(self):
        return np.trim_zeros(np.bincount(self.xs))
    
    def compute_mean(self):
        return np.mean(self.xs)

    def compute_modal(self):
        index = self.absolute_frequency.index(max(self.absolute_frequency))
        return self.xs[index]