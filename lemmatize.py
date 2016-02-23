#!/usr/bin/env python3
# coding=utf-8

from os import path
import requests

# file_names = ['smer', 'siet', 'kdh', 'olano', 'most-hid', 'sas']
file_names = ['olano']

url = 'http://text.fiit.stuba.sk:8080/lematizer/services/lemmatizer/lemmatize/fast'
headers = {'Content-Type': 'text/plain'}
d = path.dirname(__file__)

for file_name in file_names:
    data = open(path.join(d, 'programy/' + file_name + '.txt')).read()
    r = requests.post(url, data.encode('utf-8'), headers=headers)
    content = r.content.decode('utf-8')
    open(path.join(d, 'programy/' + file_name + '-lemma.txt'), 'w').write(content)
    print('Done: {}\n'.format(file_name))

