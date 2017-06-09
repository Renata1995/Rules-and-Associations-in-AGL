from info_extraction import InfoExtractor
import os,sys
import numpy as np
from scipy import stats

if len(sys.argv) <= 1:
    src = "RE_data"
else:
    src = sys.argv[1]

info_extractor = InfoExtractor()

# test_data_letter, test_data_color, test_data = info_extractor.test_data("RE_data/SCS 1 re.txt")
# letter_ap, color_ap, overall_app = info_extractor.accuracy_percent(test_data_letter, test_data_color)
# letter_cs, color_cs = info_extractor.cs_percent(test_data_letter, test_data_color)
# print letter_ap, color_ap, overall_app
# print str(letter_cs), str(color_cs)

for src in ["CFG", "RE"]:
    cs_low_avg = []
    cs_med_avg = []
    cs_high_avg = []
    for fname in os.listdir(src):
        filename = src + "/" + fname
        test_data_letter, test_data_color, test_data = info_extractor.test_data(filename)

        letter_cs, color_cs = info_extractor.cs_percent(test_data_letter, test_data_color)
        cs_low_avg.append(np.average(color_cs[0]))
        cs_med_avg.append(np.average(color_cs[1]))
        cs_high_avg.append(np.average(color_cs[2]))

        print "Chunk Strength: letter - " + str(letter_cs) + "   color: " + str(color_cs)
        print "------------------------------------\n"

    print "\nOverall cs low: Mean " + str(np.average(cs_low_avg)) + "  SD: " + str(np.std(cs_low_avg))
    print "Overall cs med: Mean " + str(np.average(cs_med_avg)) + "  SD: " + str(np.std(cs_med_avg))
    print "Overall cs high: Mean " + str(np.average(cs_high_avg)) + "  SD: " + str(np.std(cs_high_avg))
    cs_f, cs_p = stats.f_oneway(cs_low_avg, cs_med_avg, cs_high_avg)
    print "CS ANOVA  F: " + str(cs_f) + "  p: " + str(cs_p)
    print "\n-------------------------------------------------------------------------------------------------------\n"



