from info_extraction import InfoExtractor
import numpy as np
import os

# open all files
#src_list = ["CFG_SCS", "CFG_SSC", "RE_SCS", "RE_SSC", "RE_RCS", "RE_RSC", "CFG_RSC", "CFG_RCS"]
src_list = ["RE_R"]
ie = InfoExtractor()
g_percents = []

for src in src_list:
    for fname in os.listdir(src):
        filename = src + "/" + fname
        test_data_letter, test_data_color, test_data = ie.test_data(filename)

        # for each file, calculate the percentage of grammatical rating in letter items, color items, and all items
        letter_p = ie.percent_of_g(test_data_letter)
        color_p = ie.percent_of_g(test_data_color)
        all_p = ie.percent_of_g(test_data)

        g_percents.append({"letter": letter_p, "color": color_p, "all": all_p})

# display results
print np.average([p["letter"] for p in g_percents])
print np.average([p["color"] for p in g_percents])
print np.average([p["all"] for p in g_percents])

