import numpy as np

from Manipulation.chunks import CSCalculator
from utils import helper_methods as helper

re_stimuli = helper.get_learning_items("RE")
cfg_stimuli = helper.get_learning_items("CFG")

# init two CSCalculators
re_cs = CSCalculator(re_stimuli)
cfg_cs = CSCalculator(cfg_stimuli)
#
# # find all possible strings with letter_length 5 to letter_length 8 inclusively
# all_str = helper.get_all_str(5, 9)
#
# # Calculate
# re_cs_list = []
# for item in all_str:
#     cs = re_cs.chunk_strength(item)
#     re_cs_list.append(cs)
# re_cs_list = list(sorted(re_cs_list))
#
# print "RE\nAverage: " + str(np.average(re_cs_list))
# print "Median: " + str(np.median(re_cs_list))
# print "Max: " + str(max(re_cs_list))
# print "Min: " + str(min(re_cs_list))
# print "1/3 " + str(re_cs_list[len(re_cs_list)/3])
# print "2/3 " + str(re_cs_list[len(re_cs_list)*2/3])
#
# cfg_cs_list = []
# for item in all_str:
#     cs = cfg_cs.chunk_strength(item)
#     cfg_cs_list.append(cs)
#
# cfg_cs_list = list(sorted(cfg_cs_list))
# print "CFG\nAverage: " + str(np.average(cfg_cs_list))
# print "Median: " + str(np.median(cfg_cs_list))
# print "Max: " + str(max(cfg_cs_list))
# print "Min: " + str(min(cfg_cs_list))
# print "1/3 " + str(cfg_cs_list[len(cfg_cs_list)/3])
# print "2/3 " + str(cfg_cs_list[len(cfg_cs_list)*2/3])

# Calculate CS for all RE grammatical items
ifile = open(helper.get_gug_file("RE"))
ifile.readline()  # the first line is "RE"
ifile.readline()  # the second line is "G"
current = ifile.readline()
re_gitems = []
while "UG" not in current:
    re_gitems.append(current)
    current = ifile.readline()
re_g_cs = []
for item in re_gitems:
    re_g_cs.append(re_cs.chunk_strength(item))
re_g_cs = list(sorted(re_g_cs))
print "RE G items:  Average: " + str(np.average(re_g_cs))
print "Median: " + str(np.median(re_g_cs))
print "Max: " + str(max(re_g_cs))
print "Min: " + str(min(re_g_cs))
print "1/3 " + str(re_g_cs[len(re_g_cs)/3])
print "2/3 " + str(re_g_cs[len(re_g_cs)*2/3])

# --------------------------------------
# Calculate CS for all CFG grammatical items
# read all grammatical items
ifile = open(helper.get_gug_file("CFG"))
ifile.readline()  # the first line is "CFG"
ifile.readline()  # the second line is "G"

current = ifile.readline()
cfg_gitems = []
while "UG" not in current:
    cfg_gitems.append(current)
    current = ifile.readline()

# calculate cs for each item
cfg_g_cs = []
for item in cfg_gitems:
    cfg_g_cs.append(cfg_cs.chunk_strength(item))
cfg_g_cs = list(sorted(cfg_g_cs))

# calculate stats of all grammatical items
print "CFG G items:  Average: " + str(np.average(cfg_g_cs))
print "Median: " + str(np.median(cfg_g_cs))
print "Max: " + str(max(cfg_g_cs))
print "Min: " + str(min(cfg_g_cs))
print "1/3 " + str(cfg_g_cs[len(cfg_g_cs)/3])
print "2/3 " + str(cfg_g_cs[len(cfg_g_cs)*2/3])



