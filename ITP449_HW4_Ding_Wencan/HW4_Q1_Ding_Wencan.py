# Wencan Ding
# ITP449 Spring 2022
# HW4
# Q1
from matplotlib import pyplot as plt
import numpy as np
x =[]
y =[]
# generating 200 random numbers for x
for i in range(0,200):
    number = np.random.randint(1,200)
    x.append(number)
# generating 200 random numbers for y
for i in range(0,200):
    number = np.random.randint(1,200)
    y.append(number)
plt.scatter(x,y, marker="o",color="red")
plt.xlabel("Random integer")
plt.ylabel("Random integer")
plt.title("Scatter of random integers")
plt.show()