# Convert raw data files into .csv files
from info_extraction import InfoExtractor
import os
import sys

if len(sys.argv) <= 1:
    src = "RE"
else:
    src = sys.argv[1]

ie = InfoExtractor()

# open two output files for letter and color items.
# write the column names for each file
ofile_letter = open("csv files/" + src.lower() + "_letter.csv", "w")
ofile_letter.write("\"pid\";\"grammar\";\"s_type\";\"stimulus\";\"response\";\"reaction_time\";\"cs\";\"grammatical\";\"accuracy\"\n")

ofile_color = open("csv files/" + src.lower() + "_color.csv", "w")
ofile_color.write("\"pid\";\"grammar\";\"s_type\";\"stimulus\";\"response\";\"reaction_time\";\"cs\";\"grammatical\";\"accuracy\"\n")

# write data into csv files
for counter, fname in enumerate(os.listdir(src)):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = ie.test_data(filename)

    for item in test_data_letter:
        ofile_letter.write(str(counter+1) + ";" + item.write() + "\n")

    for item in test_data_color:
        ofile_color.write(str(counter+1) + ";" + item.write() + "\n")

