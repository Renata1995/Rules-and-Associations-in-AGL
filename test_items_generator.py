import os
import sys
from nltk import CFG, nonterminals, RecursiveDescentParser
import distance as dist
from Manipulation.chunks import CSCalculator
from utils import helper_methods as helper

"""
python test_items_generator.py <grammar> <output>
<grammar> could be "RE" or "CFG"
<output> is the name of the output file

"""
if len(sys.argv) <= 1:
    grammar = "RE"
else:
    if sys.argv[1] == "C":
        grammar = "CFG"
    else:
        grammar = "RE"

if len(sys.argv) <= 2:
    output = helper.get_cs_output_filename("RE")
else:
    if sys.argv[2] == "C":
        output = helper.get_cs_output_filename("CFG")
    else:
        output = helper.get_cs_output_filename("RE")

# Two grammars
re_grammar = "^[AD]*(BA|BD(A|B)*D|C(A|B)*D)$"
S, X, T = nonterminals("S, X, T")
cfg = CFG.fromstring("""
S -> X S X | T S | X | T
X -> 'A'|'B'
T -> 'C'|'D'
""")
rd_parser = RecursiveDescentParser(cfg)

# Get Training List
stimuli = helper.get_learning_items(grammar)

# Create a cs_calculator
cs_cal = CSCalculator(stimuli)

# Get all strings with length from 5 to 8
all_str = helper.get_all_str(5,9)

# Split items into three list with different CS
g_items = [[], [], []]
ug_items = [[], [], []]

for item in all_str:
    if grammar == "RE":
        if re_grammar.findall(re_grammar, item):
            item_list = g_items
        else:
            item_list = ug_items

    elif grammar == "CFG":
        tree = rd_parser.parse(item)
        if len(list(tree)) == 0:
            item_list = ug_items
        else:
            item_list = g_items

    cs = cs_cal.chunk_strength(item)
    if cs < 4.5:
        item_list[0].append(item)
    elif 4.5 <= cs <= 6.5:
        item_list[1].append(item)
    elif cs > 6.5:
        item_list[2].append(item)

# Write stimuli with different chunks to file
ofile = open(output, "w")
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
