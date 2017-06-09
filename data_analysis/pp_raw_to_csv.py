# Convert raw data files into .csv files
from info_extraction import InfoExtractor, Participant
import os
import sys

if len(sys.argv) <= 1:
    src = "RE"
else:
    src = sys.argv[1]

ie = InfoExtractor()

# open two output files for letter and color items.
# write the column names for each file
ofile_letter = open("csv files/" + src.lower() + "_pp.csv", "w")
ofile_letter.write("\"pid\";\"grammar\"")
for num in range(1, 49):
    ofile_letter.write(";" + "\"Q" + str(num)+"\"")
ofile_letter.write("\n")

# write data into csv files
src_list = {"RE", "CFG"}
counter = 1
for src in src_list:
    for fname in os.listdir(src):
        filename = src + "/" + fname
        pp = Participant(filename, counter)
        ofile_letter.write(pp.write()+"\n")
        counter += 1