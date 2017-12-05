import os
import corpus_generator
import corpus_statistics
import tokenization
import corpus_stemming
import util
import BM25
import smooth_query_likelihood
import tf_idf

unigram_index = {}
query_list = {}
bm25 = {}
tfidf = {}
query_likelihood = {}
common_words = []
given_files = 'Given_files'

# corpus_generator.generate_corpus()
# unigram_index = tokenization.create_inverted_list()
corpus_stemming.stem_corpus()