# -*- coding: utf-8 -*-
'''
NDL - THON Twitter Analytics
Author: Yuya Jeremy Ong (yuyajeremyong@gmail.com)
'''
import re
import sys
import json
import string
from math import log, exp

reload(sys)
sys.setdefaultencoding('utf8')

''' 1: Importing & Parsing Dataset '''
'''
# TODO: Write the routine to import the dataset.

print '[TOTAL TWEETS LOADED]: ' + str(len(data))
print '\n[SAMPLE TWEET]:\n'+ data[0]['text'] + '\n'
'''

''' Part 2: Text Preprocessing '''
'''
# Preprocessing Regex
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    # emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
    r'[\U00010000-\U0010ffff]' #emoji
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

# TODO: Write the routine to import the dataset.

print '[TOKENIZED SAMPLE]:\n' + str(tokens[0]) + '\n'
'''

''' Part 3: Text Filtering '''
'''
# Perform Preprocessing Routines
tokens = map(lambda tok: [t.lower() for t in tok], tokens)                                          # Text Normalization
tokens = map(lambda x: filter(None, [token.rstrip(string.punctuation) for token in x]), tokens)     # Punctuation Removal
tokens = map(lambda tok: filter(lambda x: not x.startswith('http'), tok), tokens)                   # HTTP Link Removal
tokens = map(lambda tok: filter(lambda x: not x.startswith('#'), tok), tokens)                      # Hashtag Removal
tokens = map(lambda tok: filter(lambda x: not x.startswith('@'), tok), tokens)                      # Username Removal
tokens = map(lambda tok: filter(lambda x: x.lower() != 'rt', tok), tokens)                          # RT Token Removal
tokens = map(lambda tok: filter(lambda x: len(x) > 1, tok), tokens)                                 # Remove Single Characters

print '[FILTERED TOKENS]:\n' + str(tokens[0]) + '\n'
'''

''' Part 4: Stopword Removal '''
'''
# TODO: Write the stopword removal process.

print '[STOPWORD REMOVED TOKENS]:\n' + str(tokens[0]) + '\n'
'''

''' Part 5: Compute Token Frequency '''
'''
counts = dict()
for tweet in tokens:
    # TODO: Write the frequency analysis routine

'''

''' Part 6: Sort Token Frequency '''
'''
# TODO: Write the token frequency sort routine.

print '[SORTED TOKEN FREQUENCY]:\n' + str(sorted_freq[:20]) + '\n'
'''

''' Part 7: Sentiment Analysis '''
'''
# TODO: Write the sentiment corpus loading routine.
pos_terms = open('data/pos_terms.txt', 'rb').read().split('\n')[:-1]
neg_terms = open('data/neg_terms.txt', 'rb').read().split('\n')[:-1]

print '[SCORE]: ' + str(score)
'''
