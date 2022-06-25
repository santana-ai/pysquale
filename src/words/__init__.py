import os
import sys

file = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.realpath(file)))

from .utils import get_abbreviation_list, get_punctuation_list, get_punctuation_string, get_stopwords, get_abbreviation_map

ABBREVIATION_MAP = get_abbreviation_map()
ABBREVIATION_LIST = get_abbreviation_list()
PUNCTUATION_LIST = get_punctuation_list()
PUNCTUATION_STRING = get_punctuation_string()
STOPWORDS = get_stopwords()