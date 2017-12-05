
import os
import re
import corpus_generator
import corpus_statistics
import tokenization
import util
import BM25
import smooth_query_likelihood
import tf_idf

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
            with open('Stemmed_Corpus'+'/CACM-'+ str(count)+'.txt','w+') as f:
                f.write(words)
                f.close()
                count +=1
