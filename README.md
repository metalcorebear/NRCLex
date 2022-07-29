# NRCLex

(C) 2019 Mark M. Bailey

## About
NRCLex will measure emotional affect from a body of text.  Affect dictionary contains approximately 27,000 words, and is based on the National Research Council Canada (NRC) affect lexicon (see link below) and the NLTK library's WordNet synonym sets.

Lexicon source is (C) 2016 National Research Council Canada (NRC) and this package is **for research purposes only**. Source: http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm As per the terms of use of the NRC Emotion Lexicon, if you use the lexicon or any derivative from it, cite this paper: Crowdsourcing a Word-Emotion Association Lexicon, Saif Mohammad and Peter Turney, Computational Intelligence, 29 (3), 436-465, 2013.

NLTK data is (C) 2019, NLTK Project.  Source: [NLTK] (https://www.nltk.org/).  Reference: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

## Update
* Expanded NRC lexicon from approximately 10,000 words to 27,000 based on WordNet synonyms.
* Minor bug fixes.
* Contributor updated NTC library.

## Installation
`pip install NRCLex`

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

`from nrclex import NRCLex`<br><br>


*#Instantiate text object (for best results, 'text' should be unicode).*<br>

`text_object = NRCLex('text')`<br><br>


*#Return words list.*<br>

`text_object.words`<br><br>


*#Return sentences list.*<br>

`text_object.sentences`<br><br>


*#Return affect list.*<br>

`text_object.affect_list`<br><br>


*#Return affect dictionary.*<br>

`text_object.affect_dict`<br><br>


*#Return raw emotional counts.*<br>

`text_object.raw_emotion_scores`<br><br>


*#Return highest emotions.*<br>

`text_object.top_emotions`<br><br>


*#Return affect frequencies.*<br>

`text_object.affect_frequencies`