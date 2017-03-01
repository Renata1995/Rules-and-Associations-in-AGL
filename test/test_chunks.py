from unittest import TestCase
from Manipulation.chunks import CSCalculator


class TestChunks(TestCase):
    def setUp(self):
        strlist = ["abbcc","cddab","dcbba"]
        self.csCalculator = CSCalculator(strlist)

    def test_gen_bigrams(self):
        self.assertEqual(self.csCalculator.gen_bigrams("abbcc"),["ab","bb","bc","cc"])
        self.assertEqual(self.csCalculator.gen_bigrams("ababd"),["ab","ba","ab","bd"])

    def test_gen_trigrams(self):
        self.assertEqual(self.csCalculator.gen_trigrams("abbcc"),["abb","bbc","bcc"])

    def test_init(self):
        self.assertEqual(len(self.csCalculator.chunk_dict.keys()), 19)
        self.assertEqual(self.csCalculator.chunk_dict["ab"],2)
        self.assertTrue("cda" not in self.csCalculator.chunk_dict)

    def test_chunk_strength(self):
        self.assertEqual(self.csCalculator.chunk_frequency("ab"), 2)
        self.assertEqual(self.csCalculator.chunk_frequency("cd"), 1)

    def test_avg_cs(self):
        self.assertEqual(self.csCalculator.chunk_strength("abbc"), 1.4)
