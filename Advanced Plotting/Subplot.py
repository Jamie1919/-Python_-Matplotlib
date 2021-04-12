import matplotlib.pyplot as plt
import numpy as np 

x = [1,2,3]
y = [1,2,3]

fig = plt.figure()
fig.suptitle('Plot Title')

plt.subplot(2,2,1)
plt.plot(x,y, color='purple')
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(2,2,2)
plt.plot(x,y, color='black')
plt.xlabel('x2')
plt.ylabel('y2')

plt.subplot(2,2,3)
plt.plot(x,y, color='blue')
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(2,2,4)
plt.plot(x,y, color='red')
plt.xlabel('x2')
plt.ylabel('y2')

# subplot(nrows, ncols, index, **kwargs)

plt.show()