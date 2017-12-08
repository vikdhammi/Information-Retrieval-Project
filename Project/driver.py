import os
import corpus_generator
import corpus_statistics
import tokenization
import corpus_stemming
import util
import BM25
import smooth_query_likelihood
import tf_idf
import Stopping

unigram_index = {}
query_list = {}
bm25 = {}
tfidf = {}
query_likelihood = {}
given_files = 'Given_files'

corpus_generator.generate_corpus()
unigram_index = tokenization.create_inverted_list()

#Unigram index for stemmed corpus
unigram_index= Stopping.stopping(unigram_index)

corpus_stemming.stem_corpus()