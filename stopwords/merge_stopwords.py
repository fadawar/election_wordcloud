#!/usr/bin/env python2
from os import path

MERGED_FILE_NAME = '../slovak-stopwords.txt'

files = ['stopwords_file.txt',
         'stop-words_slovak_1_sk.txt',
         'stop-words_slovak_2_sk.txt']

words = set()

for file_name in files:
    with open(path.join(path.dirname(__file__), file_name)) as f:
        for line in f:
            words.add(line.strip())

with open(path.join(path.dirname(__file__), MERGED_FILE_NAME), 'w') as f:
    for word in sorted(words):
        f.write(word + '\n')
