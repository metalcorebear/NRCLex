#!/usr/bin/env python
"""
@author: metalcorebear
"""

# Determine word affect based on the NRC emotional lexicon


from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer, PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from collections import Counter
import csv


def load(txt_file, colname = None):
    reader = csv.reader(txt_file, delimiter='\t')
    firstrow = next(reader)
    emotions = [
        'anger', 'anticipation', 'disgust', 'fear',
        'joy', 'negative', 'positive', 'sadness',
        'surprise', 'trust'
        ]
    lex = {}

    try:
        head = {
            **{x: firstrow.index(x) for x in emotions},
            **{x: firstrow.index(x) for x in firstrow if x not in emotions}
            }
    except ValueError:
        head = None

    if head:
        col = head[colname] if colname else head[firstrow[-1]]

        for row in reader:
            values = [x for x in emotions if row[head[x]] == '1']

            if values:
                lex[row[col]] = values
    else:
        if firstrow[2] == '1':
            lex[firstrow[0]] = [firstrow[1]]

        for row in reader:
            if row[2] == '1':
                if row[0] not in lex:
                    lex[row[0]] = []

                lex[row[0]].append(row[1])

    return lex


def __expand_lexicon__(self):
    vectors = []
    n_words = len(self.words)

    for i in range(n_words):
        if i + 2 < n_words:
            vectors.append(
                f'{self.words[i]} {self.words[i+1]} {self.words[i+2]}')
        if i + 1 < n_words:
            vectors.append(f'{self.words[i]} {self.words[i+1]}')
        if i < n_words:
            vectors.append(self.words[i])

    for i in set(vectors):
        if i in self.__lexicon__:
            continue

        found = False
        splits = i.split()
        use_antonyms = False

        if len(splits) > 1 and (splits[0] == 'not' or "n't" in splits[0]):
            use_antonyms = True
            context = '_'.join(splits[1:])
        else:
            context = i.replace(' ', '_')

        for j in wordnet.synsets(context):
            for k in set(j.lemmas()):
                meaning = None

                if use_antonyms:
                    antonyms = k.antonyms()

                    if antonyms:
                        meaning = antonyms[0].name().replace('_', ' ')
                else:
                    meaning = k.name().replace('_', ' ')

                if meaning in self.__lexicon__:
                    self.__lexicon__[i] = self.__lexicon__[meaning]
                    found = True
                    break

            if found:
                break

        if found:
            continue


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
    for phrase in self.words_and_phrases:
        if phrase in lexicon_keys:
            affect_list.extend(self.__lexicon__[phrase])
            affect_dict.update({phrase: self.__lexicon__[phrase]})
    for phrase in affect_list:
        affect_frequencies[phrase] += 1
    sum_values = sum(affect_frequencies.values())
    affect_percent = {'fear': 0.0, 'anger': 0.0, 'anticipation': 0.0, 'trust': 0.0, 'surprise': 0.0, 'positive': 0.0,
                      'negative': 0.0, 'sadness': 0.0, 'disgust': 0.0, 'joy': 0.0}
    for key in affect_frequencies.keys():
        affect_percent.update({key: float(affect_frequencies[key]) / float(sum_values)})
    self.affect_list = affect_list
    self.affect_dict = affect_dict
    self.raw_emotion_scores = dict(affect_frequencies)
    self.affect_frequencies = affect_percent


def words_and_phrases(self):
    words_and_phrases = []
    n_words = len(self.words)
    i = 0

    while i < n_words:
        if i + 2 < n_words:
            phrase = f'{self.words[i]} {self.words[i+1]} {self.words[i+2]}'

            if phrase in self.__lexicon__:
                words_and_phrases.append(phrase)
                i += 3
        if i + 1 < n_words:
            phrase = f'{self.words[i]} {self.words[i+1]}'

            if phrase in self.__lexicon__:
                words_and_phrases.append(phrase)
                i += 2
        if i < n_words:
            words_and_phrases.append(self.words[i])
            i += 1

    self.words_and_phrases = words_and_phrases


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

    def __init__(self, lex_filename, colname = None):
        with open(lex_filename, 'r') as txt_file:
            self.__lexicon__ = load(txt_file, colname)


    def load_token_list(self, token_list):
        '''
        Load an already tokenized text (as a list of tokens) into the NRCLex object.
        This is for when you want to use NRCLex with a text that you prefer to tokenize and/or lemmatize yourself.

        Parameters:
            token_list (list): a list of utf-8 strings.
        Returns:
            self
        '''
        self.text = ""
        self.words = token_list
        self.words_and_phrases = token_list
        self.sentences = []
        __expand_lexicon__(self)
        __build_word_affect__(self)
        top_emotions(self)

        return self


    def load_raw_text(self, text):
        '''
        Load a string into the NRCLex object for tokenization

        Parameters:
            text (str): a utf-8 string.
        Returns:
            self
        '''

        wln = WordNetLemmatizer()
        tt = TweetTokenizer()
        pst = PunktSentenceTokenizer()

        self.text = text
        self.words = [wln.lemmatize(x, 'v') for x in tt.tokenize(text)]
        self.sentences = pst.tokenize(text)

        __expand_lexicon__(self)
        words_and_phrases(self)
        __build_word_affect__(self)
        top_emotions(self)

        return self
