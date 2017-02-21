import str_gen as sg
import distance as dist
import os
import re
import sys
from nltk import CFG, nonterminals, RecursiveDescentParser
from Manipulation.chunks import ChunkStrengthCal

if len(sys.argv) <= 1:
    training = "RE.txt"
else:
    if sys.argv[1] == "R":
        training = "RE.txt"
    else:
        training = "CFG.txt"

if len(sys.argv) <= 2:
    items_after_dist = "re_dist_ge2.txt"
else:
    if sys.argv[2] == "R":
        items_after_dist = "re_dist_ge2.txt"
    elif sys.argv[2] == "C":
        items_after_dist = "cfg_dist_ge2.txt"
    else:
        items_after_dist = sys.argv[2]

if len(sys.argv) <= 3:
    cs_groups = "re_csgroups.txt"
else:
    if sys.argv[2] == "R":
        cs_groups = "re_csgroups.txt"
    else:
        cs_groups = "cfg_csgroups.txt"


re_grammar = "^[AD]*(BA|BD(A|B)*D|C(A|B)*D)$"
S, X, T = nonterminals("S, X, T")
cfg = CFG.fromstring("""
S -> X S X | T S | X | T
X -> 'A'|'B'
T -> 'C'|'D'
""")
rd_parser = RecursiveDescentParser(cfg)

# Generate all strings with 5 to 8 letters
allstr = []
for num in range(5, 9):
    allstr.extend(sg.generate_strings(num))

# -----------------------------------------------------------
# Get Training List
stimuli = dist.get_stimuli(training)

# Create two cs_calculators
cs_cal = ChunkStrengthCal(stimuli)

# Open output file
after_dist = []
if os.path.exists(items_after_dist):
    ifile = open(items_after_dist,"r")
    for line in ifile:
        after_dist.append(line.strip())
    ifile.close()
else:
    ofile = open(items_after_dist,"w")
    for item in allstr:
        if dist.sp_distance(item, stimuli):
            ofile.write(item + "\n")
            after_dist.append(item)
    ofile.close()

# Split items into three list with different CS
gitems = [[],[],[]]
ugitems = [[],[],[]]
for item in after_dist:
    cs = cs_cal.avg_cs(item)
    # if re.findall(re_grammar,item):
    #     itemlist = gitems
    # else:
    #     itemlist = ugitems
    tree = rd_parser.parse(item)
    if len(list(tree)) == 0:
        itemlist = ugitems
    else:
        itemlist = gitems

    if cs < 4.5:
        itemlist[0].append(item)
    elif 4.5 <= cs <= 6.5:
        itemlist[1].append(item)
    elif cs > 6.5:
        itemlist[2].append(item)

ofile = open(cs_groups,"w")
ofile.write("G\n")
ofile.write("Low CS\n")
for item in gitems[0]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nMed CS\n")
for item in gitems[1]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nHigh CS\n")
for item in gitems[2]:
    ofile.write(item + "\n")

ofile.write("\n-------------------------------------------\nUG\n")
ofile.write("Low CS\n")
for item in ugitems[0]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nMed CS\n")
for item in ugitems[1]:
    ofile.write(item + "\n")
ofile.write("\n----------------------------------------------------------\nHigh CS\n")
for item in ugitems[2]:
    ofile.write(item + "\n")
