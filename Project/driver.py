import Stopping
import corpus_generator
import corpus_stemming
from Phase1.Task1 import tokenization

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