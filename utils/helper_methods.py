from Queue import Queue
import os
test_location = "materials/test/"
learning_location = "materials/learning/"

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







