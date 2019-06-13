import numpy as np
from math import sqrt

one = np.array([[0], [1]])
zero = np.array([[1], [0]])

class Qubit:
    def __init__(self, a=1.0, b=0.0):
        self.a = a
        self.b = b
        self.state = self.a*zero + self.b*one


    def H(self):
        self.state = np.dot((1/sqrt(2)) * np.array([[1,  1],
                                                    [1, -1]]),
                            self.state)

    def X(self):
        self.state = np.dot(np.array([[0, 1],
                                      [1, 0]]),
                                     self.state)

    def Y(self):
        self.state = np.dot(np.array([[0, -1j],
                                      [1j, 0]]),
                            self.state)


    def Z(self):
        self.state = np.dot(np.array([[1, 0 ],
                                      [0, -1]]),
                            self.state)
