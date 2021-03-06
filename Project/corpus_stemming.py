import os
import re


def stem_corpus():

    if not os._exists('Stemmed_Corpus'):
        os.makedirs('Stemmed_Corpus')

    with open('Given_files/'+'stem_test.txt','r') as stemmed_file:
        count = 1
        text = stemmed_file.read()
        text = text.lower()
        text = text.replace('\n',' ')
        text = re.split(r'#\s[0-9]*',text)
        for words in text[1:]:
            if (' am ' or ' pm ') in words:
                words = words.split(' pm ' or ' am ')[0]
                words = words + ' pm ' + ' am '
            with open('Stemmed_Corpus'+'/CACM-'+ str(count)+'.txt','w+') as f:
                f.write(words)
                f.close()
                count +=1

