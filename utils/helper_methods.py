from Queue import Queue


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
        filename = "materials/grammar/RE.txt"
    elif condition == "CFG":
        filename = "materials/grammar/CFG.txt"

    ifile = open(filename)
    all_items = [line for line in ifile]
    return all_items






