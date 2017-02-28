class InfoExtractor:
    """
    InforExtractor provides methods to convert the raw data file into expected formats
    """
    def __init(self):
        """
        Init basic parameters in the infoExtractor
        """
        self.size_of_test_items = 24
        self.size_of_training_items = 24

    def text_to_data(self, raw):
        """
        Convert raw text into TestDataEntry objects
        :param raw: raw text
        :type raw: string
        :return: A TestDataEntry object
        """
        srt_data = TestDataEntry(raw[0], raw[1], raw[8], int(raw[10]), int(raw[19]), int(raw[26]))
        return srt_data

    def test_data(self, filename):
        """
        Extract test data from the raw data file and convert to needed list of TestDataEntry objects
        :param filename: the name of raw data file. A raw data file contains performance of a given participant
        :type filename: string
        :return: three lists of TestDataEntry objects
        test_data_letter: test data whose s_type is "Letter"
        test_data_color: test data whose s_type is "Color"
        test_data: all test data
        """
        # open the raw data file
        ifile = open(filename)

        # skip data at the learning session
        current = ifile.readline()
        while "Middle Instruction 2" not in current:
            current = ifile.readline()

        # collect data at the test session
        test_data_color = []
        test_data_letter = []

        current = ifile.readline()
        while "Debriefing" not in current: # "Debriefing" is in the last line

            # each line in the raw data file contains a given participant's response to a given test item
            entry = self.text_to_data(current.split())  # turn the current line of data into a TestDataEntry object

            # put the entry object into appropriate lists
            if entry.s_type == "Color":
                test_data_color.append(entry)
            elif entry.s_type == "String":
                test_data_letter.append(entry)

            # go to the next line
            current = ifile.readline()

        # In the experiment, test items were presented in a random order.
        # Sort test items by IDs
        test_data_color = sorted(test_data_color, key=lambda x: x.stimulus)
        test_data_letter = sorted(test_data_letter, key=lambda x: x.stimulus)

        # combine test_data_color and test_data_letter into a single list
        test_data = test_data_letter + test_data_color
        return test_data_letter, test_data_color, test_data

    def accuracy(self, test_data_letter, test_data_color):
        """
        Calculate accuracy-related values of letter test items, color test items, and all items
        :return:letter_accuracy, color_accuracy, overall_accuracy
        :rtype: three tuples
        """
        letter_accuracy = self.accuracy_helper(test_data_letter)
        color_accuracy = self.accuracy_helper(test_data_color)
        overall_accuracy = self.accuracy_helper(test_data_letter + test_data_color)

        return letter_accuracy, color_accuracy, overall_accuracy

    def accuracy_helper(self, data):
        """
        A helper method to calculate accuracy
        :param data: a list of TestDataEntry objects
        :return: an accuracy dictionary
        accuracy["g"]: The number of correct judgments on grammatical items
        accuracy["g_percent"]: The percentage of correct judgments on grammatical items
        accuracy["ug"]: The number of correct judgments on ungrammatical items
        accuracy["ug_percent"]: The percentage of correct judgments on ungrammatical items
        accuracy["overall"]: The number of correct judgments on all items
        accuracy["percent"]: The percentage of correct judgments on all items
        :rtype: dictionary
        """
        accuracy = {"g": 0, "ug": 0}

        for item in data:
            if item.stimulus < 13: # grammatical items
                if self.grammatical(item.response):
                    accuracy["g"] += 1
            else: # ungrammatical items
                if not self.grammatical(item.response):
                    accuracy["ug"] += 1

        accuracy["overall"] = accuracy["g"] + accuracy["ug"]
        accuracy["percent"] = float(accuracy["overall"])/len(data)
        accuracy["g_percent"] = float(accuracy["g"]) * 2/len(data)
        accuracy["ug_percent"] = float(accuracy["ug"]) * 2 / len(data)
        print accuracy["g_percent"]

        return accuracy

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


class TestDataEntry:
    """
    The TestDataEntry class contains information about each participant's performance.
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

