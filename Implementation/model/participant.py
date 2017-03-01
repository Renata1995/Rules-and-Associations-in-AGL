class Participant:
    """
    The Participant class collects basic demographic information and responses of participants
    """
    def __init__(self, id, age, gender):
        self.id = id
        self.age = age
        self.gender = gender

        # Response in the grammar session.
        # A list of LearningDataEntry objects
        self.learning_session_input = []

        # Response in the test session
        # A list of TestDataEntry objects
        self.test_session_input = []
