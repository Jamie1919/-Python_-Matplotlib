X = []
Y = []

with open('values.txt', 'r') as myfile:
	for line in myfile:
		Yappend( int(line) )

X = list(range(0, len(Y)+1))
print(X)
print(Y)