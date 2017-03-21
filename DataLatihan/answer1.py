data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

# Jawaban
# --------
sensor =  ['I', 'and', 'The', 'you']
tersensor = ['*' * len(kata) if kata in sensor else kata for kata in readData(data1)]
print(' '.join(tersensor))