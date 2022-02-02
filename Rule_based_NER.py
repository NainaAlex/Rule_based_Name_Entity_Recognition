import numpy as np
import pandas as pd
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = ['European authorities fined Google a record '+
'$5.1 billion on Wednesday for abusing its power in '+
'the mobile phone market and ordered the company to alter its practices']

print(ex)