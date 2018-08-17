%matplotlib inline

from matplotlib import pyplot as plt

data = [[3, 1.5, 1], 
        [2, 1, 0],
        [4, 1.5, 1],
        [3, 1, 0],
        [3.5, 0.5, 1],
        [2, 0.5, 0],
        [5.5, 1, 1],
        [1, 1, 1]]
mysteryFlower = [4.5, 1]

weight1 = np.random.randn()
weight2 = np.random.randn()
bias = np.random.rand()

#sigmoid functions

def sigmoid(x):
    return (1/(1+np.exp(-x)))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

#scatter the data
for i in range(len(data)):
  point = data[i]
  color = "r"
  if point[2] == 0:
    color = "b"
  plt.scatter(point[0], point[1], c = color)
  
T = np.linspace(-5, 5, 20)
Y = sigmoid (T)
Z = sigmoid_p(T)
plt.plot(T,Y, c = 'r')
plt.plot(T,Z, c = 'b')

