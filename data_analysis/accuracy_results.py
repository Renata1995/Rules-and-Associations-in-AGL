from info_extraction import InfoExtractor
import os,sys
import numpy as np
from scipy import stats

if len(sys.argv) <= 1:
    src = "CFG"
else:
    src = sys.argv[1]

if len(sys.argv) <= 2:
    output = src + "_accuracy_results.txt"
else:
    output = sys.argv[2]

info_extractor = InfoExtractor()

# open the output file
ofile = open(output, "w")

for fname in os.listdir(src):
    ac_avg = []

    ac_color_avg = []
    ac_letter_avg = []

    ac_grammatical_avg = []
    ac_ungrammatical_avg = []

    for fname in os.listdir(src):
        filename = src + "/" + fname
        ofile.write("Participant ID: " + fname.replace(".txt", "") + "\n")

        # extract data from the raw file
        test_data_letter, test_data_color, test_data = info_extractor.test_data(filename)

        # calculate accuracy of letter test items, color test items, and all test items
        letter_ap, color_ap, overall_ap = info_extractor.accuracy(test_data_letter, test_data_color)

        # Grammatical Items
        ofile.write("Grammatical Items: \n")
        ofile.write("Letter   number:  " + str(letter_ap["g"]) + " percent: " + str(letter_ap["g_percent"]))
        ofile.write("   Color number: " + str(color_ap["g"]) +  "  percent: " + str(color_ap["g_percent"]))
        ofile.write("   Overall number:  " + str(overall_ap['g']) + "  percent: " + str(overall_ap["g_percent"]) + "\n\n")

        # Ungrammatical Items
        ofile.write("Ungrammatical Items: \n")
        ofile.write("Letter   number:  " + str(letter_ap["ug"]) + " percent: " + str(letter_ap["ug_percent"]))
        ofile.write("   Color number: " + str(color_ap["ug"]) + "  percent: " + str(color_ap["ug_percent"]))
        ofile.write("   Overall number:  " + str(overall_ap['ug']) + "  percent: " + str(overall_ap["ug_percent"]) + "\n\n")

        # All Items
        ofile.write("All Items: \n")
        ofile.write("Letter   number:  " + str(letter_ap["overall"]) + " percent: " + str(letter_ap["percent"]))
        ofile.write("   Color number: " + str(color_ap["overall"]) + "  percent: " + str(color_ap["percent"]))
        ofile.write("   Overall number:  " + str(overall_ap['overall']) + "  percent: " + str(overall_ap["percent"]) + "\n")

        ac_avg.append(overall_ap['percent'])

        ac_color_avg .append(color_ap["percent"])
        ac_letter_avg.append(letter_ap["percent"])

        ac_grammatical_avg.append(overall_ap["g_percent"])
        ac_ungrammatical_avg.append(overall_ap["ug_percent"])

        ofile.write("------------------------------------\n\n")

    # summary
    ofile.write("Overall avg " + str(np.average(ac_avg)) + "  SD: " + str(np.std(ac_avg)))
    ofile.write("\nLetter avg " + str(np.average(ac_letter_avg)) + "  SD: " + str(np.std(ac_letter_avg)))
    ofile.write("\nColor avg " + str(np.average(ac_color_avg)) + "  SD: " + str(np.std(ac_color_avg)))

    ofile.write("\nGrammatical avg " + str(np.average(ac_grammatical_avg)) + "  SD: " + str(np.std(ac_grammatical_avg)))
    ofile.write("\nUngrammatical avg " + str(np.average(ac_ungrammatical_avg)) + "  SD: " + str(np.std(ac_ungrammatical_avg)))



