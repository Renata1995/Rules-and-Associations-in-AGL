import sys
from Manipulation.chunks import CSCalculator
from utils import helper_methods as helper
import random

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
#ofile = open(helper.get_cs_output_filename(grammar), "w")
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
# ofile.write(grammar + "\n")
# ofile.write("G\n")
# ofile.write("Low CS\n")
# for item in g_items[0]:
#     ofile.write(item + "\n")
# ofile.write("\n----------------------------------------------------------\nMed CS\n")
# for item in g_items[1]:
#     ofile.write(item + "\n")
# ofile.write("\n----------------------------------------------------------\nHigh CS\n")
# for item in g_items[2]:
#     ofile.write(item + "\n")
#
# ofile.write("\n-------------------------------------------\nUG\n")
# ofile.write("Low CS\n")
# for item in ug_items[0]:
#     ofile.write(item + "\n")
# ofile.write("\n----------------------------------------------------------\nMed CS\n")
# for item in ug_items[1]:
#     ofile.write(item + "\n")
# ofile.write("\n----------------------------------------------------------\nHigh CS\n")
# for item in ug_items[2]:
#     ofile.write(item + "\n")

# randomly select test items
g_test = []   # 3 (cs level: low, med, high) x 4 (letter letter_length: 5, 6, 7, 8)
for cs_level in range(0, 3):
    g_test.append([])
    for letter_length in range(0, 4):
        g_test[cs_level].append([])

for cs_level, cs_list in enumerate(g_items):
    for letter_length in range(5, 9):
        for num in range(0, 4):
            item = random.choice(cs_list)
            while len(item) != letter_length:
                item = random.choice(cs_list)
            g_test[cs_level][letter_length - 5].append(item)
            cs_list.remove(item)

ug_test = []   # 3 (cs level: low, med, high) x 4 (letter letter_length: 5, 6, 7, 8)
for cs_level in range(0, 3):
    ug_test.append([])
    for letter_length in range(0, 4):
        ug_test[cs_level].append([])

for cs_level, cs_list in enumerate(ug_items):
    for letter_length in range(5, 9):
        for num in range(0, 4):
            item = random.choice(cs_list)
            while len(item) != letter_length:
                item = random.choice(cs_list)
            ug_test[cs_level][letter_length - 5].append(item)
            cs_list.remove(item)

ofile = open(helper.test_location + grammar + "_test.txt", "w")
# write grammatical items
ofile.write(grammar + "\nG\n")
for cs_level, cs_list in enumerate(g_test):
    for letter_length, item_list in enumerate(cs_list):
        ofile.write(item_list[0] + "\n")
        for num in range(1, 4):
            ofile.write(ug_test[cs_level][letter_length][num] + "\n")
        ofile.write("\n")

# write ungrammatical items
ofile.write("\nUG\n")
for cs_level, cs_list in enumerate(ug_test):
    for letter_length, item_list in enumerate(cs_list):
        ofile.write(item_list[0] + "\n")
        for num in range(1, 4):
            ofile.write(g_test[cs_level][letter_length][num] + "\n")
        ofile.write("\n")



