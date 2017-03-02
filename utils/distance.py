from nltk.metrics import distance as dist


def get_stimuli(filename):
    str_list = []
    ifile = open(filename)
    for line in ifile:
        str_list.append(line.strip())
    return str_list


def avg_distance(string, stimuli):
    distance_sum = 0
    for item in stimuli:
        distvalue = dist.edit_distance(string, item)
        distance_sum += distvalue
    return distance_sum/len(stimuli)


def sp_distance(string,stimuli):
    for item in stimuli:
        if dist.edit_distance(string, item) < 2:
            return False
    return True





