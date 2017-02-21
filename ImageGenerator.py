from PIL import Image, ImageDraw
import distance as dist
import os

unit = 100
abcd = ["A.","B.","C.","D."]

def letter_to_color(letter):
    if letter == "A":
        return "rgb(230,0,0)"
    elif letter == "B":
        return "rgb(252,251,52)"
    elif letter == "C":
        return "rgb(0,175,0)"
    elif letter == "D":
        return "rgb(25,128,255)"

def letter_convert(letter):
    if letter == "A":
        return "R"
    elif letter == "B":
        return "Y"
    elif letter == "C":
        return "G"
    elif letter == "D":
        return "B"

def rename(letters):
    newstr = ""
    for index, item in enumerate(letters):
        newstr += letter_convert(item)
    return newstr

def gen_image(letters, filename):
    length = len(letters)
    im = Image.new("RGB", (length*unit, unit), "white")
    draw = ImageDraw.Draw(im)
    gap = 10
    for index, letter in enumerate(letters):
        x1 = unit * index + gap
        y1 = gap
        x2 = unit * (index+1) - gap
        y2 = unit - gap
        color = letter_to_color(letter)
        draw.ellipse((x1, y1, x2, y2), fill=color, outline=color)
    im.save(filename)

# os.makedirs("RE")
# re_stimuli = dist.get_stimuli("RE.txt")
# os.makedirs("CFG")
# cfg_stimuli = dist.get_stimuli("CFG.txt")
# #
# # for item in re_stimuli:
# #     gen_image(item, "RE/" + rename(item) + ".jpg")
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