import os
from utils import distance as dist
from utils import helper_methods as helper




# os.makedirs("RE_SCS")
# re_stimuli = dist.get_stimuli("RE_SCS.txt")
# os.makedirs("CFG")
# cfg_stimuli = dist.get_stimuli("CFG.txt")
# #
# # for item in re_stimuli:
# #     gen_image(item, "RE_SCS/" + rename(item) + ".jpg")
# for item in cfg_stimuli:
#     gen_image(item, "CFG/" + rename(item) + ".jpg")

if not os.path.exists("RETEST"):
    os.makedirs("RETEST")
else:
    for pic in os.listdir("RETEST"):
        del pic
re_test = dist.get_stimuli("re_test_items.txt")
for index, item in enumerate(re_test):
    gen_image(item, "RETEST/test"+rename(item)+".jpg")

os.makedirs("CFGTEST")
cfg_test = dist.get_stimuli("cfg_test_items.txt")
for index, item in enumerate(cfg_test):
    gen_image(item, "CFGTEST/test"+rename(item)+".jpg")