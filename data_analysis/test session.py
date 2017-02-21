from info_extraction import InfoExtractor
import os,sys

if len(sys.argv) <= 1:
    src = "RE_data"
else:
    src = sys.argv[1]

info_extractor = InfoExtractor()

# test_data_letter, test_data_color, test_data = info_extractor.test_data("RE_data/SCS 3.txt")
# letter_ap, color_ap, overall_app = info_extractor.accuracy_percent(test_data_letter, test_data_color)
# letter_cs, color_cs = info_extractor.cs_percent(test_data_letter, test_data_color)
# print letter_ap, color_ap, overall_app
# print str(letter_cs), str(color_cs)
print "RE"
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = info_extractor.test_data(filename)
    letter_ap, color_ap, overall_app = info_extractor.accuracy_percent(test_data_letter, test_data_color)
    letter_cs, color_cs = info_extractor.cs_percent(test_data_letter, test_data_color)
    print "Letter: " + str(letter_ap) +"   Color: " + str(color_ap) + "   Overall: " + str(overall_app)
    print "------------------------------------\n"

print "CFG"
src = "CFG_data"
for fname in os.listdir(src):
    filename = src + "/" + fname
    test_data_letter, test_data_color, test_data = info_extractor.test_data(filename)
    letter_ap, color_ap, overall_app = info_extractor.accuracy_percent(test_data_letter, test_data_color)
    letter_cs, color_cs = info_extractor.cs_percent(test_data_letter, test_data_color)
    print "Letter: " + str(letter_ap) +"   Color: " + str(color_ap) + "   Overall: " + str(overall_app)
    print "------------------------------------\n"