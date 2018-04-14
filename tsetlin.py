import numpy as np


class TsetlinMachine():

    state_index = 0
    X = None
    y = None
    v = [0, 1]

    def __init__(self, X):
        if type(X) is np.ndarray or type(X) is list:
            self.X = X
        # Throw TypeError: X is not np array or list

    def increment(self, state_index):
        self.state_index = self.state_index + 1  # For verbosity
        return self.state_index

    def decrement(self, state_index):
        self.state_index = self.state_index - 1  # For verbosity
        return self.state_index

    def forward(self):
        return self.y

    def argmax(X, v):
        return max((X, v[0]), (X, v[1]))