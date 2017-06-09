# Rule-based Processing and Association-based Processing in Artificial Grammar Learning

## Table of Contents
 * Introduction
 * Requirements

## Introduction

### Question
In our daily life, different forms of knowledge are involved.  
* Rule-based knowledge
	i.e. When we try to identify whether an integer x is oddd or even, we use a specific rule: x%2==0? Even:Odd
* Association-based knowledge
	i.e. classical conditioning, operant conditioning

Based on the form of knowledge, two learning and decision making processes are proposed, rule-based learning and association-based learning.
In the learning phase, rule-based learning stores abstract rules wherease association-based learning stores associations.
When a new case comes, rule-based learning considers whether the new case satisfies a specific rule and then gives a corresponding result. Association-based learning checks whether the new case could trigger stored associations. A judgment depends on the number of triggered associations and the intensity of each association.

![Learning and decision making](/image/learning.png)

The current experiment investigates how a rule-based variable and an association-based variable influence human performance in a simplified experimental setting of learning, the artificial grammar learning paradigm.

### ARTIFICIAL GRAMMAR LEARNING PARADIGM (AGL)

* #### Basic Question
  The artifical grammar learning paradigm is a simplified learning-test experimental setting. After exposure to strings derived from a formal grammar, human participants illustrated above-chance accuracy on grammatical judgments of new strings without knowledge in details of the grammar (Reber, 1967). 
  Strings derived from a formal grammar exhibit not only rule-based patterns but also statistical/associative features. 
  AGL research investigates what type of knowledge, rule-based or association-based or both, has been learned  

* #### Implementation
  Prepare a formal grammar (AG): most researchers used finite state grammars

* ##### Training Phase:
  * Participants will observe/memorize a set of items generated by the AG
  * Participants will not be told that strings follow certain rules

* ##### Test Phase:
  * A list of new items is generated. X% follows the AG (Grammatical-G) and 1-x% does not (Ungrammatical-UG)
  * Participants will be told that training strings follow a certain grammar but not details of the grammar
  * Participants will be asked to determine whether new items are grammatical or ungrammarical

* ##### Transfer Setting
Learning items and test items use the same grammatical rules but different alphabets.
i.e. The learning session uses letter sequences and the test session uses color sequences.

* ##### Normal Results:
  * Participants exhibit above chance accuracy
  * Participants could not articulate how they make grammaticality judgments.

* ##### Various Interpretations
    * Rule-Based Interpretations
        * Participants have learned complete or partial of the original grammar ([Reber,1967](http://www.wjh.harvard.edu/~pal/pdfs/replaced_scanned_articles/reber67_scanned.pdf),[1969](http://psycnet.apa.org/psycinfo/1969-12199-001), [1989](http://www.wjh.harvard.edu/~pal/pdfs/pdfs/reber89.pdf))
        * Participants have learned a set of propositional rules with the form {Feature -> Grammaticality} ([Dulany, et al, 1984](http://www.wjh.harvard.edu/~pal/pdfs/pdfs/dulany84.pdf))

            Feature refers to a chunk of symbols. Grammaticality refers to "Grammatical" or "Ungrammatical"

            i.e. A participant might learned that items with the chunk "XV" are always grammatical and establishes the rule {"XV" -> Grammatical}

    * Statistics-Based Interpretations
        * Specific Similarity/Edit Distance: Grammatical judgment of a given test item is based on whether the test item is highly similar to a specific learning item ([Vokey & Brooks, 1992](http://www.wjh.harvard.edu/~pal/pdfs/replaced_scanned_articles/vokey-brooks92_scanned.pdf))
        * Generalized Context Model: Grammatical judgment of a given test item is based on the averaged similarity between the test item and all learning items ([Pothos & Bailey, 2000](https://www.researchgate.net/profile/Todd_Bailey/publication/12375156_The_Role_of_Similarity_in_Artificial_Grammar_Learning/links/5405ac020cf2c48563b17c30/The-Role-of-Similarity-in-Artificial-Grammar-Learning.pdf))
        * Analogical Similarity: Grammatical judgment of a transfer test item is based on structural similarity with learning items ([Brooks & Vokey](http://www.wjh.harvard.edu/~pal/pdfs/pdfs/brooks-vokey91.pdf))
        * Chunk Strength: Grammatical judgment of a given test item is based on whether the test item contains frequent bigrams or trigrams([Knowlton & Squire, 1996](http://www.wjh.harvard.edu/~pal/pdfs/pdfs/knowlton-squire96.pdf))
        * Entropy: Grammatical judgment of a given test item is based on its entropy value according to all learning items ([Jamieson et al., 2016](https://www.ncbi.nlm.nih.gov/pubmed/25828458))

### PRESENT EXPERIMENT

#### Independent Variables
1. Grammar Complexity:
    * Finite State grammar
    * Context Free Grammar
2. Chunk Strength: For a given item, chunk strength is the averaged frequency of all its bigrams and trigrams in the learning session

#### Experiment Design
Both standard and transfer settings are used

2 (Grammatical vs. Ungrammatical) x 3 (High, Medium & Low Chunk Strength) x 2 (Changed Module vs. Unchanged Module)

![experiment design](/image/exp_design.png)

## Requirements
* [NLTK](http://www.nltk.org/)
* [NumPy](http://www.numpy.org/)
