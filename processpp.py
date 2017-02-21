ifile = open("pp.txt")
ofile = open ("newpp.txt","w")

for line in ifile:
	ofile.write(line+";")