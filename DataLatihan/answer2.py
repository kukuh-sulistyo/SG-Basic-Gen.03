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
hasil = [kata for kata in readData(data1) if kata in readData(data2)] # menghasilkan list berisi kata yang sama
for kata in set(hasil): print(kata, hasil.count(kata)) # output hasil
