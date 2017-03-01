from Manipulation.chunks import ChunkStrengthCal
import numpy as np
import distance as dist
import str_gen as sg

re_stimuli = dist.get_stimuli("RE_SCS.txt")
cfg_stimuli = dist.get_stimuli("CFG_SCS.txt")

re_cs = ChunkStrengthCal(re_stimuli)
cfg_cs = ChunkStrengthCal(cfg_stimuli)

allstr = []
for num in range(5, 9):
    allstr.extend(sg.generate_strings(num))

vlist = []
file = open("re_cs_test.txt","w")
for item in allstr:
    rev = re_cs.avg_cs(item)
    file.write(str(rev) + "\n")
    vlist.append(rev)
print "RE_SCS" + str(np.average(vlist))
print str(max(vlist))
print str(min(vlist))

# cfglist = []
# file = open("cfg_cs_test.txt","w")
# for item in allstr:
#     rev = cfg_cs.avg_cs(item)
#     file.write(str(rev) + "\n")
#     cfglist.append(rev)
# print "CFG" + str(np.average(cfglist))

