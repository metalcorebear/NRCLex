# NRCLex

(C) 2019 Mark M. Bailey

## About
NRCLex will measure emotional affect from a body of text.  Affect dictionary contains approximately 27,000 words, and is based on the National Research Council Canada (NRC) affect lexicon (see link below) and the NLTK library's WordNet synonym sets.

Lexicon source is (C) 2016 National Research Council Canada (NRC) and this package is **for research purposes only**.  Source: [lexicons for research] (http://sentiment.nrc.ca/lexicons-for-research/)

NLTK data is (C) 2019, NLTK Project.  Source: [NLTK] (https://www.nltk.org/).  Reference: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

## Update
* Expanded NRC lexicon from approximately 10,000 words to 27,000 based on WordNet synonyms.
* Minor bug fixes.

## Affects
Emotional affects measured include the following:

* fear
* anger
* anticipation
* trust
* surprise
* positive
* negative
* sadness
* disgust
* joy

## Sample Usage

from nrclex import NRCLex  


*#Instantiate text object (for best results, 'text' should be unicode).*  

text_object = NRCLex('text')  


*#Return words list.*  

text_object.words  


*#Return sentences list.*  

text_object.sentences  


*#Return affect list.*  

text_object.affect_list  


*#Return affect dictionary.*  

text_object.affect_dict  


*#Return raw emotional counts.*  

text_object.raw_emotion_scores  


*#Return highest emotions.*  

text_object.top_emotions  


*#Return affect frequencies.*  

text_object.affect_frequencies  