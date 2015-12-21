#!/usr/bin/env python3
"""
Generates words from tri-grams read from a dictionaries.
"""
import random
import sys

class Trigrams:

    def __init__(self, filename):
        self._ngram_count = 0

        ngrams = []
        with open(filename, "r") as dictionary:
            for line in dictionary:
                ngrams += self.read_trigrams(line)

        self.build_readdb(ngrams)

    def __str__(self):
        return repr(self._ngrams)

    def read_bigrams(self, line):
        start = 0
        end = 2
        bigrams=[]
        while end < len(line):
            bigrams.append(line[start:end].lower())

            start += 1
            end += 1

        return bigrams

    def read_trigrams(self, line):
        start = 0
        end = 3
        trigrams=[]
        while end < len(line):
            trigrams.append(line[start:end].lower())

            start += 1
            end += 1

        return trigrams

    def read_quadgrams(self, line):
        start = 0
        end = 4
        quadgrams=[]
        while end < len(line):
            quadgrams.append(line[start:end].lower())

            start += 1
            end += 1

        return quadgrams

    def build_readdb(self, ngrams):
        ngramdb = {}
        frequencies = {}
        start_list = []
        ngram_lists = {}

        for ngram in ngrams:
            prefix = ngram[0:-1]
            suffix = ngram[-1]

            start_list.append(prefix)

            if prefix not in ngramdb:
                ngramdb[prefix] = {}
                frequencies[prefix] = 0
                ngram_lists[prefix] = []

            frequencies[prefix] += 1
            ngram_lists[prefix] += suffix

            if suffix in ngramdb[prefix]:
                ngramdb[prefix][suffix] += 1
            else:
                ngramdb[prefix][suffix] = 1

        self._ngramdb = ngramdb
        self._frequencies = frequencies

        self._start_list = start_list
        self._ngram_lists = ngram_lists

    def random_first(self):
        return random.choice(self._start_list)

    def next_character(self, prefix):
        return random.choice(self._ngram_lists[prefix])

def main():
    if len(sys.argv) != 3:
        print("Usage: {} word_length dictionary\nDictionary is a file containing a word per line with no non-alphabetic characters.".format(sys.argv[0]))
    else:
        random.random()
        grams = Trigrams(sys.argv[2])

        #Generate a word
        word = grams.random_first()

        while len(word) < sys.argv[1]:
            word += grams.next_character(word[-2:])

        print(word)



main()
