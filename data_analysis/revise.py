file = open("RE_data/SCS 2 new.txt")
ofile = open("RE_data/SCS 2 re.txt", "w")
for num in range(6):
    file.readline()
for line in file:
    texts = line.split()
    texts.pop(3)
    line = " ".join(texts)
    ofile.write(line + "\n")
