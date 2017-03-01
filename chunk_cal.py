import numpy as np

import distance as dist
from Manipulation.chunks import CSCalculator
from utils import helper_methods as helper

re_stimuli = helper.get_learning_items("RE")
cfg_stimuli = helper.get_learning_items("CFG")

# init two CSCalculators
re_cs = CSCalculator(re_stimuli)
cfg_cs = CSCalculator(cfg_stimuli)

# find all possible strings with length 5 to length 8 inclusively
all_str = []
for num in range(5, 9):
    all_str.extend(helper.all_str_with_length(num))

# Calculate
vlist = []
file = open("re_cs_test.txt","w")
for item in all_str:
    rev = re_cs.chunk_strength(item)
    file.write(str(rev) + "\n")
    vlist.append(rev)
print "RE_SCS" + str(np.average(vlist))
print str(max(vlist))
print str(min(vlist))

# cfglist = []
# file = open("cfg_cs_test.txt","w")
# for item in all_str:
#     rev = cfg_cs.avg_cs(item)
#     file.write(str(rev) + "\n")
#     cfglist.append(rev)
# print "CFG" + str(np.average(cfglist))

