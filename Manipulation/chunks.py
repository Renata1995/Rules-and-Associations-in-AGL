import numpy as np


class ChunkStrengthCal:
    """
    The ChunkStrengthCal class calculate the chunk strength of a given item
    A chunk is defined as adjacent co-occurring letters in a sequence, such as a bigram or a trigram


    """
    def __init__(self, str_list):
        self.chunk_dict = self.strlist_to_bigrams(str_list)
        self.chunk_dict.update(self.strlist_to_trigrams(str_list))


    def gen_bigrams(self, string):
        """
        Extract all bigrams in a given string
        Repetition of a bigram is counted as different bigrams
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
        Convert a list of strings into a list of bigrams by decomposing each string into a list of bigrams
        :param str_list: a list of strings
        :return: a list of bigrams
        """
        cdict = {}
        for item in str_list:
            clist = self.gen_bigrams(item)
            for bigram in clist:
                if bigram not in cdict:
                    cdict[bigram] = 1
                else:
                    cdict[bigram]+=1
        return cdict

    def strlist_to_trigrams(self, str_list):
        """
        Convert a list of strings into a list of trigrams by decomposing each string into a list of trigrams
        :param str_list: a list of strings
        :return: a list of trigrams
        """
        cdict = {}
        for item in str_list:
            clist = self.gen_trigrams(item)
            for trigram in clist:
                if trigram not in cdict:
                    cdict[trigram] = 1
                else:
                    cdict[trigram] += 1
        return cdict

    def chunk_strength(self, chunk):
        """
        Calculate the chunk strength.
        :param chunk:
        :type chunk:
        :return:
        :rtype:
        """
        if chunk in self.chunk_dict:
            return self.chunk_dict[chunk]
        else:
            return 0

    def avg_cs(self, string):
        clist = self.gen_bigrams(string)
        clist.extend(self.gen_trigrams(string))
        vlist = []
        for item in clist:
            vlist.append(self.chunk_strength(item))
        return np.average(vlist)

