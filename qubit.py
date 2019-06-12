import numpy as np

one = np.array([[0], [1]])
zero = np.array([[1], [0]])

class Qubit:
    def __init__(self, a=1.0, b=0.0):
        self.a = a
        self.b = b
        self.state = self.a*zero + self.b*one

    def X(self):
        self.state = np.dot(np.array([[0, 1],
                                      [1, 0]]),
                                     self.state)
