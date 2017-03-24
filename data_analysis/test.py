from info_extraction import InfoExtractor
import numpy as np
import os

# open all files
ie = InfoExtractor()

src = "RE_RSC"
for fname in os.listdir(src):
    filename = src + "/" + fname
    print filename
    test_data_letter, test_data_color, test_data = ie.test_data(filename)