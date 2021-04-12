import matplotlib.pyplot as plt

values = [16,18,4,8]
pielabels = ['Python', 'Ruby', 'Java', 'SQL']
piecolors = ['purple', 'pink', 'black', 'red']
pieexplode = [0.2,0,0,0.1]

plt.pie(values,labels=pielabels,explode=pieexplode, colors =piecolors, startangle=90,shadow=True)
plt.title('Pie Chart')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.legend(loc='best')
plt.show()