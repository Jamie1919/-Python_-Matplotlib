import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

x2 = [1,2,3,4,5]
y2 = [1,3,9,13,16]

x3 = [1,2,3,4,5]
y3 = [2,4,6,8,10]

plt.bar(x1,y1)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()