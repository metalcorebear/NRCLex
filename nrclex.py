#!/usr/bin/env python
"""
@author: metalcorebear
"""

# Determine word affect based on the NRC emotional lexicon
# Library is built on TextBlob

from textblob import TextBlob
from collections import Counter
from json import load


def __build_word_affect__(self):
    '''
    Instantiates the following attributes:
        affect_list
        affect_dict
        raw_emotion_scores
        affect_frequencies
    '''
    affect_list = []
    affect_dict = dict()
    affect_frequencies = Counter()
    lexicon_keys = self.__lexicon__.keys()
    for word in self.words:
        if word in lexicon_keys:
            affect_list.extend(self.__lexicon__[word])
            affect_dict.update({word: self.__lexicon__[word]})
    for word in affect_list:
        affect_frequencies[word] += 1
    sum_values = sum(affect_frequencies.values())
    affect_percent = {'fear': 0.0, 'anger': 0.0, 'anticipation': 0.0, 'trust': 0.0, 'surprise': 0.0, 'positive': 0.0,
                      'negative': 0.0, 'sadness': 0.0, 'disgust': 0.0, 'joy': 0.0}
    for key in affect_frequencies.keys():
        affect_percent.update({key: float(affect_frequencies[key]) / float(sum_values)})
    self.affect_list = affect_list
    self.affect_dict = affect_dict
    self.raw_emotion_scores = dict(affect_frequencies)
    self.affect_frequencies = affect_percent


def top_emotions(self):
    '''
    top_emotions becomes a list of (emotion: str, score: float) with the highest score associated to the input text.
    '''
    emo_dict = self.affect_frequencies
    max_value = max(emo_dict.values())
    top_emotions = []
    for key in emo_dict.keys():
        if emo_dict[key] == max_value:
            top_emotions.append((key, max_value))
    self.top_emotions = top_emotions


class NRCLex:
    """Lexicon source is (C) 2016 National Research Council Canada (NRC) and library is for research purposes only.  Source: http://sentiment.nrc.ca/lexicons-for-research/"""

    def __init__(self, lexicon_file='nrc_en.json'):
        with open(lexicon_file, 'r') as json_file:
            self.__lexicon__ = load(json_file)

    def load_token_list(self, token_list):
        '''
        Load an already tokenized text (as a list of tokens) into the NRCLex object.
        This is for when you want to use NRCLex with a text that you prefer to tokenize and/or lemmatize yourself.

        Parameters:
            token_list (list): a list of utf-8 strings.
        Returns:
            No return
        '''
        self.text = ""
        self.words = token_list
        self.sentences = []
        __build_word_affect__(self)
        top_emotions(self)

    def load_raw_text(self, text):
        '''
        Load a string into the NRCLex object for tokenization and lemmatization with TextBlob.

        Parameters:
            text (str): a utf-8 string.
        Returns:
            No return
        '''
        self.text = text
        blob = TextBlob(self.text)
        self.words = [w.lemmatize() for w in blob.words]
        self.sentences = list(blob.sentences)
        __build_word_affect__(self)
        top_emotions(self)