from info_extraction import InfoExtractor
import os
from scipy import stats
import matplotlib.pyplot as plt

# open all files
ie = InfoExtractor()

src = "CFG"
# g items
re_letter_g = []
re_color_g = []
re_all_g = []
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = ie.test_data(filename)
    letter_ap, color_ap, overall_ap = ie.accuracy(test_data_letter, test_data_color)
    re_letter_g.append(letter_ap["g_percent"])
    re_color_g.append(color_ap["g_percent"])
    re_all_g.append(overall_ap["g_percent"])

# ug items
re_letter_ug = []
re_color_ug = []
re_all_ug = []
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = ie.test_data(filename)
    letter_ap, color_ap, overall_ap = ie.accuracy(test_data_letter, test_data_color)
    re_letter_ug.append(letter_ap["ug_percent"])
    re_color_ug.append(color_ap["ug_percent"])
    re_all_ug.append(overall_ap["ug_percent"])

# construct a comparison list
re_comp = []
for item in re_letter_g:
    re_comp.append(0.5)

src = "CFG_R"
rec_letter_g = []
rec_color_g = []
rec_all_g = []
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = ie.test_data(filename)
    letter_ap, color_ap, overall_ap = ie.accuracy(test_data_letter, test_data_color)
    rec_letter_g.append(letter_ap["g_percent"])
    rec_color_g.append(color_ap["g_percent"])
    rec_all_g.append(overall_ap["g_percent"])

# ug items
rec_letter_ug = []
rec_color_ug = []
rec_all_ug = []
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = ie.test_data(filename)
    letter_ap, color_ap, overall_ap = ie.accuracy(test_data_letter, test_data_color)
    rec_letter_ug.append(letter_ap["ug_percent"])
    rec_color_ug.append(color_ap["ug_percent"])
    rec_all_ug.append(overall_ap["ug_percent"])

# construct a comparison list
rec_comp = []
for item in rec_letter_g:
    rec_comp.append(0.5)


# Whether RE - G items are different than 50%
lresult = stats.ttest_ind(re_letter_g, re_comp)
cresult = stats.ttest_ind(re_color_g, re_comp)
allresult = stats.ttest_ind(re_all_g, re_comp)
print "RE  Letter-G: " + str(lresult) + "  Color-G: " + str(cresult) + "  All-G: " + str(allresult)

lresult = stats.ttest_ind(re_letter_ug, re_comp)
cresult = stats.ttest_ind(re_color_ug, re_comp)
allresult = stats.ttest_ind(re_all_ug, re_comp)
print "RE  Letter-UG: " + str(lresult) + "  Color-UG: " + str(cresult) + "  All-UG: " + str(allresult)

lresult = stats.ttest_ind(rec_letter_g, rec_comp)
cresult = stats.ttest_ind(rec_color_g, rec_comp)
allresult = stats.ttest_ind(rec_all_g, rec_comp)
print "REC Letter-G: " + str(lresult) + "  Color-G: " + str(cresult) + "  All-G: " + str(allresult)

lresult = stats.ttest_ind(rec_letter_ug, re_comp)
cresult = stats.ttest_ind(rec_color_ug, re_comp)
allresult = stats.ttest_ind(rec_all_ug, re_comp)
print "REC  Letter-UG: " + str(lresult) + "  Color-UG: " + str(cresult) + "  All-UG: " + str(allresult)

# plot
plot_list = rec_all_ug
x_axis = range(1, len(plot_list)+1)
y_axis = [item*100 for item in plot_list]

line_pos, = plt.plot(x_axis, y_axis, color=(0, 0, 1), marker="o")
plt.show()



