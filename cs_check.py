from utils import distance as dist

stimuli = dist.get_stimuli("CFG_SCS.txt")

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