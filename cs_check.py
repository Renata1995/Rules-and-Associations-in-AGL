import str_gen as sg
import distance as dist
import os
import re
import sys
from nltk import CFG, nonterminals, RecursiveDescentParser
from Manipulation.chunks import CScalculator

stimuli = dist.get_stimuli("CFG.txt")

string = """
BCDBA
ACCDCA
CBCBCAA
DBDDCCCA
ACDCA
BBCBAB
DCBDCAB
CADBDDAB
ADCAB
CABDAB
BADDDAB
DDCBBDAB
BACDD
ACCDBC
CDDCDBB
DBCBABCD
ACBBC
CADCAC
DACABBC
BCCABCAA
DBBDA
ADCBDA
BCDABDA
DDCADABD
"""

str_list = string.split()
for item in str_list:
    if item in stimuli:
        print item
# Create two cs_calculators
# cs_cal = CScalculator(stimuli)
# for item in string.split():
#     print cs_cal.avg_cs(item)