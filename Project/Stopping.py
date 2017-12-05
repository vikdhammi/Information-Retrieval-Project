
import os
import corpus_generator
import corpus_statistics
import tokenization
import util
import BM25
import smooth_query_likelihood
import tf_idf

unigram = {}
common_words = {}
def stopping():
    given_files = 'Given_Files'
    os.chdir(given_files)

    for words in open(given_files + '/' + 'common_words', 'r').readlines():
        common_words.append(words.strip('\n'))

    for each in common_words:
        if each in unigram:
            del unigram[each]

    for k,v in unigram.items():
        print(k,v)