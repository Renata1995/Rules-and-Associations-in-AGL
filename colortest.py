from PIL import Image, ImageDraw, ImageFont
import distance as dist
import os

unit = 100
abcd = ["A. ", "B. ", "C. ", "D. "]
start = 50

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
    length = len(letters[1])
    im = Image.new("RGB", (start+length*unit, unit*4), "white")
    draw = ImageDraw.Draw(im)
    gap = 10
    for row, item in enumerate(letters):
        font = ImageFont.truetype("arial.ttf", 50)
        draw.text((5, row*unit+10), abcd[row], (0,0,0), font=font)
        for index, letter in enumerate(item):
            x1 = start + unit * index + gap
            y1 = row*unit+gap
            x2 = start + unit * (index+1) - gap
            y2 = (row+1)*unit - gap
            color = letter_to_color(letter)
            draw.ellipse((x1, y1, x2, y2), fill=color, outline=color)
    im.save(filename)


re_test = dist.get_stimuli("re_test1.txt")
for num in range(len(re_test)/4):
    item = re_test[num*4:num*4+4]
    gen_image(item, "RETEST/4test"+str(num)+".jpg")