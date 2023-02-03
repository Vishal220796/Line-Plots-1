import matplotlib.pyplot as plt


x1 = [4,2,3]
y1 = [5,1,6]

plt.plot(x1, y1,color="blue", label = "Blue Line")

x2 = [5,1,4]
y2 = [6,2,1]

plt.plot(x2, y2,color="red", label = "Red Line")

x3 = [2,6,4]
y3 = [1,3,6]

plt.plot(x3, y3,color="navy", label = "Navy Line")

x4 = [5,7,3]
y4 = [3,1,6]

plt.plot(x4, y4,color="aqua", label = "Aqua Line")

x5 = [8,2,3]
y5 = [4,1,6]

plt.plot(x5, y5,color="orange", label = "Orange Line")

x6 = [9,2,3]
y6 = [8,1,2]

plt.plot(x6, y6,color="yellow", label = "Yellow Line")

x7 = [5,2,3]
y7 = [5,2,6]

plt.plot(x7, y7,color="silver", label = "Silver Line")

x8 = [7,2,1]
y8 = [1,3,2]

plt.plot(x8, y8,color="teal", label = "Teal Line")

x9 = [9,1,3]
y9 = [8,2,3]

plt.plot(x9, y9,color="fuchsia", label = "Fuchsia Line")

x10 = [3,2,1]
y10 = [4,5,6]

plt.plot(x10, y10,color="lime", label = "Lime Line")

plt.xlabel('X AXIS')

plt.ylabel('Y AXIS')

plt.title('Line Plots')

plt.legend()


plt.show()