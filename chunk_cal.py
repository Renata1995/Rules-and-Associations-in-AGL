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
all_str = helper.get_all_str(5, 9)

# Calculate
re_cs_list = []
for item in all_str:
    cs = re_cs.chunk_strength(item)
    re_cs_list.append(cs)
print "RE\nAverage: " + str(np.average(re_cs_list))
print "Median: " + str(np.median(re_cs_list))
print "Max: " + str(max(re_cs_list))
print "Min: " + str(min(re_cs_list))

cfg_cs_list = []
for item in all_str:
    cs = cfg_cs.chunk_strength(item)
    cfg_cs_list.append(cs)
print "CFG\nAverage: " + str(np.average(cfg_cs_list))
print "Median: " + str(np.median(cfg_cs_list))
print "Max: " + str(max(cfg_cs_list))
print "Min: " + str(min(cfg_cs_list))

