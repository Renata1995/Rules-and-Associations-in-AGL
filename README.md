# Thesis

#### Table of Contents
---------------------
 * Introduction
 * Requirements
 * Installation
 * FAQ

#### Introduction
---------------------
Phenomena in various fields of cognitive psychology, such as categorization, reasoning, language, and learning, could be interpreted and modeled in two conflicting perspectives, rules and similarity (Pothos, 2005). Artificial grammar learning paradigm (AGL) lies on the debate (Pothos, 2007). The rules perspective attributes grammatical judgments to learning of grammar rules. In contrast, the similarity perspective suggests that grammatical judgments depend on comparison of similarity with learned stimuli regarding each stimulus as a whole unit or discrete chunks (Pothos, 2007). Two associative networks, simple recurrent network (SRN) which distributes learned information throughout the whole network and competitive chunking network (CNN) which stores learned information locally, were used to model performances of AGL with manipulation of various variables (Boucher & Dienes, 2003; Kinder & Lotz, 2009). Previous research indicated that both networks predict the main effect and the interaction effect between chunk strength and grammaticality (Kinder & Lotz, 2009). The current study connects AGL with the formal language theory, which describes computational complexity of languages and rules, to investigate impact of grammar complexity on AGL (Sipser, 2013). A context-free grammar (CFG), which requires intermediate representations and extra memory space, has higher computational complexity than a finite state grammar (FSG) (Sipser, 2013), which was commonly used in AGL research. The current study compares a finite state grammar and a context-free grammar in both traditional and transfer conditions and varies test items by chunk strengths and grammaticality. The study uses a 3 (grammar complexity: FSG, CFG and control) ✕ 2 (stimulus modality—letter string or color sequence) ✕ 2 (grammaticality as a within subject variable) ✕ 3 (chunk strength as a within subject variable) design. Data are under collection. An interaction effect between grammar complexity and grammaticality would indicate that computational complexity of grammar rules influences AGL performance. Better performance on the CFG than the FSG would support an evolutionary explanation of AGL as human languages can be represented as CFGs but not FSGs. If SRN and CCN sufficiently predict learning performance of the CFG, then the learning of two grammars might not differ. Otherwise, learning of the CFG might require additional information processing. 

#### Requirements
---------------------
* [NLTK](http://www.nltk.org/)
* [NumPy](http://www.numpy.org/)
* [CherryPy](http://cherrypy.org/)