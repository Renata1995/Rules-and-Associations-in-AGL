class InfoExtractor:
    """
    InforExtractor provides methods to convert the raw data file into expected formats
    """
    def __init(self):
        self.size_of_test_items = 24
        self.size_of_training_items = 24

    def SRT_data(self, raw):
        srt_data = DataEntry(raw[0], raw[1], raw[8], int(raw[10]), int(raw[19]), int(raw[26]))
        return srt_data

    def test_data(self, filename):
        ifile = open(filename)

        # skip RE_data at the learning session
        current = ifile.readline()
        while "Middle Instruction 2" not in current:
            current = ifile.readline()
        # collect RE_data at the test session
        test_data_color = []
        test_data_letter = []

        current = ifile.readline()

        while "Debriefing" not in current:
            entry = self.SRT_data(current.split())
            if entry.s_type == "Color":
                test_data_color.append(entry)
            elif entry.s_type == "String":
                test_data_letter.append(entry)
            current = ifile.readline()

        test_data_color = sorted(test_data_color, key=lambda x: x.stimulus)
        test_data_letter = sorted(test_data_letter, key=lambda x: x.stimulus)

        test_data = []
        test_data.extend(test_data_letter)
        test_data.extend(test_data_color)
        return test_data_letter, test_data_color, test_data

    def test_data_random(self, filename):
        ifile = open(filename)

        # skip RE_data at the learning session
        current = ifile.readline()
        while "Random Instruction" not in current:
            current = ifile.readline()
        # collect RE_data at the test session
        test_data_color = []
        test_data_letter = []

        ifile.readline()
        current = ifile.readline()
        while "Debriefing" not in current:
            entry = self.SRT_data(current.split())
            if entry.s_type == "Color":
                test_data_color.append(entry)
            elif entry.s_type == "String":
                test_data_letter.append(entry)
            current = ifile.readline()

        test_data_color = sorted(test_data_color, key=lambda x: x.stimulus)
        test_data_letter = sorted(test_data_letter, key=lambda x: x.stimulus)

        test_data = []
        test_data.extend(test_data_letter)
        test_data.extend(test_data_color)
        return test_data_letter, test_data_color, test_data

    def accuracy_percent(self, test_data_letter, test_data_color):
        letter_ap = self.accuracy_helper(test_data_letter)
        color_ap = self.accuracy_helper(test_data_color)
        overall_ap = (letter_ap + color_ap)/2
        return letter_ap, color_ap, overall_ap

    def accuracy_helper(self, data):
        g_accuracy = 0
        ug_accuracy = 0
        for item in data:
            if item.stimulus < 13:
                if item.response == 3 or item.response == 4:
                    g_accuracy += 1
            else:
                if item.response == 1 or item.response == 2:
                    ug_accuracy += 1
        print "grammatical # of correct: " + str(g_accuracy) + "  ungrammatical # of correct: " + str(ug_accuracy)
        accuracy = g_accuracy + ug_accuracy
        print data[0].s_type + " # correct:  " + str(accuracy) + "/" + str(len(data))
        percent = float(accuracy)/len(data)
        return percent

    def cs_percent(self, test_data_letter, test_data_color):
        letter_cs = self.cs_helper(test_data_letter)
        color_cs = self.cs_helper(test_data_color)
        return letter_cs, color_cs

    def cs_helper(self, data):
        low, medium, high = 0, 0, 0
        for item in data:
            if item.stimulus in [1, 2, 3, 4, 13, 14, 15, 16]:
                if self.grammatical(item.response):
                    low += 1
            elif item.stimulus in [5, 6, 7, 8, 17, 18, 19, 20]:
                if self.grammatical(item.response):
                    medium += 1
            elif item.stimulus in [9, 10, 11, 12, 21, 22, 23, 24]:
                if self.grammatical(item.response):
                    high += 1
        low = float(low)/8
        medium = float(medium)/8
        high = float(high)/8
        return low, medium, high

    def grammatical(self, num):
        if num == 3 or num == 4:
            return True
        elif num == 1 or num == 2:
            return False


class DataEntry:
    """
    The DataEntry class contains information about each participant's performance.
    Variables:
    - grammar: The grammar experimental condition. Values: RE or CFG

    - s_type: Indicate whether the stimulus type is "Color" or "String/Letter"

    - order: The order variable consists of three letters, such as "LCL". L stands for "Letter" and C stands for "Color"
            The first letter indicates whether the training session has color items or letter items.
            The test session contains both color and letter items. The order of the second and third letter indicates
            whether color items goes first or letter items goes first.
            i.e. "LCL" means: a)the training phase has letter items  b) the test session has color items first and
             then letter items

    - stimulus: ID of the stimulus

    - response: Response of a given participants. Possible values: 1,2,3,4
              1: I am sure the current sequence does not follow the same pattern
              2: I guess the current sequence does not follow the same pattern
              3: I guess the current sequence follows the same pattern
              4: I am sure the current sequence follows the same pattern

    - reaction_time: The time from the test item is presented on the screen to a response is given


    """
    def __init__(self, grammar, order, s_type, stimulus, response, reaction_time):
        self.grammar = grammar
        self.order = order
        self.s_type = s_type
        self.stimulus = stimulus
        self.response = response
        self.reaction_time = reaction_time

    def display(self):
        print self.grammar + " " + self.order + " " + self.s_type + " " + str(self.stimulus) + " " + str(self.response) + " " + str(self.reaction_time)

