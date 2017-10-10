import networkx as nx
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
import matplotlib.pyplot as plt

# data = lil_matrix((2,2),dtype ='f')
# data[0,1] = 1.0
# data[0,0] = 3.0
# data[1,0] = 2.0
# s = data[0,:]
#
#
# print(np.random.rand(2,3))


class mydic(dict):
    def __init__(self, *args):
        dict.__init__(self, *args)
        self.name = 'mydic'
    def to_print(self):
        print(self)

    def __add__(self,other):
        if set(self.keys()) != set(other.keys()):
            raise Exception("index of vlabels is not the same")
        return mydic({node: self[node]+ other[node] for node in self})


def plot_test():
    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    y1 = []
    y2 = []
    for num in x:
        y1.append(num*num)
        y2.append(np.exp(num))
    # plot
    plt.figure(1)
    plt.plot(x, y1, color='r', label='lpa')
    plt.plot(x, y2, color='g', label='gradient')
    plt.legend(loc='upper right')
    plt.savefig('test.png')
    plt.show()

plot_test()
x=[1,2,3,4]
