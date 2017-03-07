import sys
from Manipulation.chunks import CSCalculator
from utils import helper_methods as helper

"""
python gug.py <grammar> <output>
<grammar> could be "RE" or "CFG"

"""
if len(sys.argv) <= 1:
    grammar = "RE"
else:
    if sys.argv[1] == "c":
        grammar = "CFG"
    else:
        grammar = "RE"

# input and output file
ofile = open(helper.get_cs_output_filename(grammar), "w")
ifile = open(helper.get_gug_file(grammar))

# Get learning list
stimuli = helper.get_learning_items(grammar)

# Create a cs_calculator
cs_cal = CSCalculator(stimuli)

# Split items into three list with different CS
g_items = [[], [], []]
ug_items = [[], [], []]

# Read grammatical and ungrammatical items from the input file
ifile.readline()  # the first line is the name of the current grammar
ifile.readline()  # the second line is "G"

current = ifile.readline()
while "UG" not in current:
    current = current.strip()
    g_items[helper.cs_index(current, cs_cal)].append(current)
    current = ifile.readline()

current = ifile.readline()
while "END" not in current:
    current = current.strip()
    ug_items[helper.cs_index(current, cs_cal)].append(current)
    current = ifile.readline()

# Write stimuli with different chunks to file
ofile.write(grammar + "\n")
ofile.write("G\n")
ofile.write("Low CS\n")
for item in g_items[0]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nMed CS\n")
for item in g_items[1]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nHigh CS\n")
for item in g_items[2]:
    ofile.write(item + "\n")

ofile.write("\n-------------------------------------------\nUG\n")
ofile.write("Low CS\n")
for item in ug_items[0]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nMed CS\n")
for item in ug_items[1]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nHigh CS\n")
for item in ug_items[2]:
    ofile.write(item + "\n")
