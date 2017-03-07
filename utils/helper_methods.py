from Queue import Queue
import os
from PIL import Image, ImageDraw


test_location = "materials/test/"
learning_location = "materials/learning/"
unit = 100

def all_str_with_length(length):
    """
    Generate all strings with a certain length and the alphabet ["A", "B", "C", "D"]
    :type length: int
    :return: a list strings
    """
    alphabet = ["A", "B", "C", "D"]

    str_queue = Queue()
    for letter in alphabet:
        str_queue.put(letter)

    # The expected length of the queue is 4^length.
    # Iteratively pop the queue as long as the expected length is not met
    while str_queue.qsize() != pow(4, length):
        # pop the current item
        current = str_queue.get()
        # create new strings by adding each letter to the end of the current item
        # put new items to the queue
        for index, value in enumerate(range(len(alphabet))):
            str_queue.put(current+alphabet[index])

    # transfer the str_queue into a list
    str_list = []
    for length in range(pow(4, length)):
        str_list.append(str_queue.get())

    return str_list


def get_learning_items(condition):
    """
    Get all grammar items for a specific grammar
    :param condition: "RE" or "CFG"
    :return: a list of strings
    :rtype: list
    """
    filename = ""
    if condition == "RE":
        filename = learning_location + "RE.txt"
    elif condition == "CFG":
        filename = learning_location + "CFG.txt"

    ifile = open(filename)
    all_items = [line for line in ifile]
    return all_items


def get_cs_output_filename(condition):
    """
    Return the output filename of chunk strength
    :param condition: "RE" or "CFG"
    :type condition: String
    :return: a filename
    """
    if condition == "RE":
        return test_location + "/re_csgroups.txt"
    elif condition == "CFG":
        return test_location + "/cfg_csgroups.txt"


def get_all_str(head, tail):
    """
    Return all strings with length from head(inclusive) to tail(exclusive)
    :return: a list of strings
    """
    all_str = []
    filename = "materials/all_str_" + str(head) + "_" + str(tail) + ".txt"

    if os.path.exists(filename):
        # if all strings with length from head to tail are already written on a file, retrieve all items
        ifile = open(filename, "r")
        for line in ifile:
            all_str.append(line.strip())
        ifile.close()
    else:
        # if the file does not exist, find all strings with length from head to tail and write these strings to a file
        ofile = open(filename, "w")
        for num in range(head, tail):
            all_str.extend(all_str_with_length(num))
        for item in all_str:
            ofile.write(item + "\n")
        ofile.close()

    return all_str


def letter_to_color(letter):
    """
    Transfer a letter into a color
    A corresponds to red. B corresponds to yellow. C corresponds to green. D corresponds to blue.
    :param letter: an input letter
    :type letter: string
    :return: a color
    :rtype: string
    """
    if letter == "A":
        return "rgb(230,0,0)"
    elif letter == "B":
        return "rgb(252,251,52)"
    elif letter == "C":
        return "rgb(0,175,0)"
    elif letter == "D":
        return "rgb(25,128,255)"


def letter_convert(letter):
    """
    Convert a letter to the first letter of the corresponded color
    "A" corresponds to "R"
    "B" corresponds to "Y"
    "C" corresponds to "G"
    "D" corresponds to "B"
    :param letter: a letter
    :type letter: string
    :return: a letter
    :rtype: string
    """
    if letter == "A":
        return "R"
    elif letter == "B":
        return "Y"
    elif letter == "C":
        return "G"
    elif letter == "D":
        return "B"


def rename(item):
    """
    To rename picture files
    :param item: an item containing a list of letters
    :type item: string
    "A" corresponds to "R"
    "B" corresponds to "Y"
    "C" corresponds to "G"
    "D" corresponds to "B"

    i.e.
    Input: "ABBAC"
    Output: "RYYRG"

    :return: a new string with converted letters
    :rtype: string
    """
    new_str = ""
    for index, item in enumerate(item):
        new_str += letter_convert(item)
    return new_str


def gen_image(letters, filename):
    """
    Generate an image according to a string and save to a specific filename
    In the string, A corresponds to red. B corresponds to yellow. C corresponds to green. D corresponds to blue.
    :param letters: a letter string  i.e. "AABAC"
    :type letters: string
    :param filename: filename of the generated image
    :type filename: string
    """
    length = len(letters)

    # generate an image
    im = Image.new("RGB", (length*unit, unit), "white")
    draw = ImageDraw.Draw(im)
    gap = 10

    # draw each color as a circle
    for index, letter in enumerate(letters):
        x1 = unit * index + gap
        y1 = gap
        x2 = unit * (index+1) - gap
        y2 = unit - gap
        color = letter_to_color(letter)
        draw.ellipse((x1, y1, x2, y2), fill=color, outline=color)

    # save the image
    im.save(filename)


def get_gug_file(condition):
    """
    Get the filename of which saves grammatical and ungrammatical items of a specific grammar
    :param condition: "RE" or "CFG"
    :type condition: string
    :return: a filename
    :rtype: string
    """
    if condition == "RE":
        return "materials/re_gug.txt"
    elif condition == "CFG":
        return "materials/cfg_gug.txt"




