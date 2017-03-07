import os
from utils import distance as dist
from utils import helper_methods as helper

re_test = helper.test_location + "re_color/"
cfg_test = helper.test_location + "cfg_color/"

# generate color test items for RE
if not os.path.exists(re_test):
    os.makedirs(re_test)
else:
    for pic in os.listdir(re_test):
        del pic
re_test_items = dist.get_stimuli(helper.test_location + "re_test_items.txt")
for index, item in enumerate(re_test_items):
    helper.gen_image(item, re_test + helper.rename(item)+".jpg")

# generate color test items for CFG
if not os.path.exists(cfg_test):
    os.makedirs(cfg_test)
else:
    for pic in os.listdir(cfg_test):
        del pic
cfg_test_items = dist.get_stimuli(helper.test_location + "cfg_test_items.txt")
for index, item in enumerate(cfg_test_items):
    helper.gen_image(item, cfg_test + helper.rename(item)+".jpg")