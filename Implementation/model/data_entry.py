class TestDataEntry:
    """
    A TestDataEntry object contains a given participant's performance on a given test item
    Variables:
    - id: ID of the stimulus

    - pid: ID of the Participant owner

    - grammar: The grammar experimental condition. Values: RE_SCS or CFG_SCS

    - s_type: Indicate whether the stimulus type is "Color" or "String/Letter"

    - order: The order variable consists of three letters, such as "LCL". L stands for "Letter" and C stands for "Color"
            The first letter indicates whether the training session has color items or letter items.
            The test session contains both color and letter items. The order of the second and third letter indicates
            whether color items goes first or letter items goes first.
            i.e. "LCL" means: a)the training phase has letter items  b) the test session has color items first and
             then letter items

    - response: Response of a given participants. Possible values: 1,2,3,4
              1: I am sure the current sequence does not follow the same pattern
              2: I guess the current sequence does not follow the same pattern
              3: I guess the current sequence follows the same pattern
              4: I am sure the current sequence follows the same pattern

    - reaction_time: The time from the test item is presented on the screen to a response is given


    """
    def __init__(self, pid, id, grammar, order, s_type, response, reaction_time):
        self.pid = pid
        self.stimulus = id
        self.grammar = grammar
        self.order = order
        self.s_type = s_type
        self.response = response
        self.reaction_time = reaction_time

    def display(self):
        """
        Print information about current test data entry
        """
        print self.grammar + " " + self.order + " " + self.s_type + " " + str(self.stimulus) + " " + str(self.response) + " " + str(self.reaction_time)


class LearningDataEntry:
    """
    A LearningDataEntry object contains a given participant's learning performance on a set of stimuli
    """
    def __init__(self, trials, reaction_time, num_of_stimuli):
        self.trials = trials
        self.reaction_time = reaction_time
        self.num_of_stimuli = num_of_stimuli
