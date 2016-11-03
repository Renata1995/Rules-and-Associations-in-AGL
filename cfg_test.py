import nltk
from nltk.parse import RecursiveDescentParser

S, X, T = nltk.nonterminals("S, X, T")
cfg = nltk.CFG.fromstring("""
S -> X S X | T S | X | T
X -> 'A'|'B'
T -> 'C'|'D'
""")

rd_parser = RecursiveDescentParser(cfg)
# for t in rd_parser.parse(list("ADDBA")):
#      print(t)
tree = rd_parser.parse(list("AAADDD"))
print len(list(tree))
