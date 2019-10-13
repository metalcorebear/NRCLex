#!/usr/bin/env python
"""
@author: metalcorebear
"""

#Determine word affect based on the NRC emotional lexicon
#Library is built on TextBlob

from textblob import TextBlob
from collections import Counter
import pickle


def build_word_affect(self):
    #Build word affect function
    affect_list = []
    affect_dict = dict()
    affect_frequencies = Counter()
    lexicon_keys = self.lexicon.keys()
    for word in self.words:
        if word in lexicon_keys:
            affect_list.extend(self.lexicon[word])
            affect_dict.update({word:self.lexicon[word]})
    for word in affect_list:
        affect_frequencies[word] += 1
    self.affect_list = affect_list
    self.affect_dict = affect_dict
    self.affect_frequencies = dict(affect_frequencies)

class NRCLex:

    """Lexicon source is (C) 2016 National Research Council Canada (NRC) and library is for research purposes only.  Source: http://sentiment.nrc.ca/lexicons-for-research/"""

    #lexicon = {'fawn': ['negative'], 'pardon': ['positive'], 'cussed': ['anger']}
    with open('lexicon.pkl', 'r') as pkl_file:
        lexicon = pickle.load(pkl_file)
    
    def __init__(self, text):
        self.text = text
        blob = TextBlob(text)
        self.words = list(blob.words)
        self.sentences = list(blob.sentences)
        build_word_affect(self)


    def append_text(self, text_add):
        self.text = self.text + ' ' + text_add
        blob = TextBlob(self.text)
        self.words = list(blob.words)
        self.sentences = list(blob.sentences)
        build_word_affect(self)