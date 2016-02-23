#!/usr/bin/env python2
"""
Generate wordclouds with specific colors.

colors    - list of rgb colors
file_name - path to file with source text
"""

from os import path
import random
import functools
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Smer
# colors = [(195, 27, 51)]
# file_name = 'programy/smer-lemma-simple.txt'

# Siet
colors = [(235, 90, 84), (36, 142, 186)]
file_name = 'programy/siet-lemma-simple.txt'

# KDH
# colors = [(214, 12, 26), (0, 80, 140)]
# file_name = 'programy/kdh-lemma-simple.txt'

# OLaNO
# colors = [(178, 200, 0), (72, 81, 89)]
# file_name = 'programy/olano-lemma-simple.txt'

# Most-Hid
# colors = [(245, 128, 37), (35, 31, 32)]
# file_name = 'programy/most-hid-lemma-simple.txt'

# SaS
# colors = [(166, 206, 56), (0, 132, 203), (0, 70, 125)]
# file_name = 'programy/sas-lemma-simple.txt'


# Read the whole text.
d = path.dirname(__file__)
text = open(path.join(d, file_name)).read()


def crop_rgb(num):
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num


def random_similar_color(rgb_colors, *args, **keywords):
    limit = 60
    r, g, b = random.choice(rgb_colors)
    max_part = max(r, g, b)
    new_color = lambda x: crop_rgb(x + random.randint(-limit, limit))

    if max_part == r:
        return new_color(r), g, b
    elif max_part == g:
        return r, new_color(g), b
    else:
        return r, g, new_color(b)


# function returns random color but similar to colors from parameter
color_func = functools.partial(random_similar_color, colors)

# Ignore single characters, plus list of words provided in separate file
chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]

words = []
with open('slovak-stopwords.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

ignorewords = chars + words

# Generate a word cloud image
# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(stopwords=ignorewords,
                      width=1280, height=1280,
                      background_color='white',
                      color_func=color_func,
                      # font_path='/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf',
                      prefer_horizontal=0.9,).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
