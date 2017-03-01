import numpy as np


class CSCalculator:
    """
    The CSCalculator class calculates chunk strength of a given item
    A chunk is defined as adjacent co-occurring letters in a sequence, such as a bigrams or a trigrams
    Chunk strength is defined as the sum of frequency of each chunk divided by the number of chunks

    I.e.
    In the string "ABBAC" , chunks and assumed frequency of each chunk in the grammar session are listed.
    {"AB": 2, "BB": 3", "BA": 2, "AC": 1, "ABB":0, "BBA": 3, "BAC":1}
    Chunk strength of "ABBAC" = the sum of frequency of each chunk/ the number of chunks
    = (2 + 3 + 2 + 1 + 0 + 3 + 1)/7 = 1.71
    """

    def __init__(self, learning_items):
        """
        Input all items in a grammar session to init a CSCalculator object
        :param learning_items: a list of grammar items
        :type learning_items: a list of strings

        self.chunk_dict: the dictionary of all chunks and corresponding frequency

        i.e.
        learning_items:"["ABBAC","ABBDC", "CDABB"]
        self.chunk_dict: {AB":3, "BB":3, "BA":1, "AC":1, "BD":1, "DC":1, "CD":1, "DA":1,"ABB":2, "BBA":1, "BAC":1,
        "BBD":1, "CDC":1, "CDA":1, "DAB":1, "ABB": 1 }

        """
        self.chunk_dict = self.strlist_to_bigrams(learning_items)
        self.chunk_dict.update(self.strlist_to_trigrams(learning_items))


    def gen_bigrams(self, string):
        """
        Extract all bigrams in a given string
        Repetition of a bigram is counted as different bigrams

        i.e.
        Input : "ABBAC"
        Output: ["AB", "BB", "BA", "AC"]

        :return: all bigrams in the input string
        :rtype: a list of strings
        """
        clist = []
        for index, value in enumerate(string[:-1]):
            next = string[index+1]
            bigram = value + next
            clist.append(bigram)
        return clist

    def gen_trigrams(self, string):
        """
        Extract all trigrams in a given string

        i.e.
        Input : "ABBAC"
        Output: ["ABB", "BBA", "BAC"]

        :return: all trigrams in the input string
        :rtype: a list of strings
        """
        clist = []
        for index, value in enumerate(string[:-2]):
            next = string[index+1]
            nn = string[index+2]
            trigram = value + next + nn
            clist.append(trigram)
        return clist

    def strlist_to_bigrams(self, str_list):
        """
        List all bigrams in a list of strings and the frequency of each bigram

         i.e.
        Input : "["ABBAC","ABBDC", "CDABB"]
        Output: {"AB":3, "BB":3, "BA":1, "AC":1, "BD":1, "DC":1, "CD":1, "DA":1}

        :param str_list: a list of strings
        :return: a dictionary with key as bigrams and values as frequencies
        """
        freq_dict = {}

        for item in str_list:

            # Find all bigrams in the current item
            bigrams = self.gen_bigrams(item)

            for bigram in bigrams:
                # if the bigram does not exist in the dictionary, add it to the dictionary
                if bigram not in freq_dict:
                    freq_dict[bigram] = 1
                else:
                    # if the bigram exist in the dictionary, add 1 to the frequency value
                    freq_dict[bigram] += 1

        return freq_dict

    def strlist_to_trigrams(self, str_list):
        """
        List all trigrams in a list of strings and the frequency of each trigram

        i.e.
        Input : "["ABBAC","ABBDC", "CDABB"]
        Output: {"ABB":2, "BBA":1, "BAC":1, "BBD":1, "CDC":1, "CDA":1, "DAB":1, "ABB": 1}

        :param str_list: a list of strings
        :return: a dictionary of trigrams and frequency
        """
        freq_dict = {}
        for item in str_list:
            # Find all trigrams in the current item
            trigrams = self.gen_trigrams(item)

            for trigram in trigrams:
                # if the current trigram is not in the dictionary, add it to the dictionary with a frequency value 1
                if trigram not in freq_dict:
                    freq_dict[trigram] = 1
                else:
                    # if the current trigram is in the dictionary, increase the value of frequency by 1
                    freq_dict[trigram] += 1

        return freq_dict

    def chunk_frequency(self, chunk):
        """
        Calculate the frequency of a chunk in the grammar session.

        i.e.
        Input: "AB"
        Output: 4

        :param chunk: a bigram or trigram
        :type chunk: string
        :return: a frequency number
        """
        if chunk in self.chunk_dict:
            return self.chunk_dict[chunk]
        else:
            return 0

    def chunk_strength(self, test_string):
        """
        Calculate the chunk strength of a string.
        Chunk strength is defined as the sum of frequency of each bigram or trigram divided by the number of chunks

        I.e.
        In the string "ABBAC" , chunks and assumed frequency of each chunk in the grammar session are listed.
        {"AB": 2, "BB": 3", "BA": 2, "AC": 1, "ABB":0, "BBA": 3, "BAC":1}
        Chunk strength of "ABBAC" = the sum of frequency of each chunk/ the number of chunks
        = (2 + 3 + 2 + 1 + 0 + 3 + 1)/7 = 1.71
        :type test_string: string
        :return: chunk strength of the test_string
        :rtype: float
        """
        # Get all bigrams in the test_string
        clist = self.gen_bigrams(test_string)
        # Get all trigrams in
        clist.extend(self.gen_trigrams(test_string))

        # Find frequency of each chunk in the grammar session
        freq_list = []
        for item in clist:
            freq_list.append(self.chunk_frequency(item))

        return np.average(freq_list)

