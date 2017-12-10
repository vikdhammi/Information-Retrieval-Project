import operator
import os
from collections import defaultdict, OrderedDict
from functools import partial

from Phase1.Task1 import tokenization
from Phase1.Task1.BM25 import bm25_scoring


class PseudoRelevance(object):
    def __init__(self, corpus_path, ranker, n):
        self.corpus_path = corpus_path
        self.ranker = ranker
        # top n doc required
        self.n = n

    def search(self, search_term):
        results = self.ranker(search_term)
        ii_list = []
        for index, file_path in enumerate(results):
            print(file_path)
            ii_list.append(
                self._get_inverted_index(os.path.join(self.corpus_path, file_path) + '.txt')[0]
            )

            if index == self.n:
                break

        common_words = self._get_common_words(ii_list, self.n)
        new_words = [w for w in common_words.keys()[:self.n]]
        new_search_term = search_term + " ".join(new_words)

        new_results = self.ranker(new_search_term)

        for i, r in enumerate(new_results):
            print(r)
            if i == 10:
                break

    def _get_common_words(self, idf_list, n):
        common_words = defaultdict(int)
        for idf in idf_list:
            for term in idf:
                common_words[term] += idf[term][0][1]  # Result contains [docid, count]. Get count.

        return OrderedDict(sorted(common_words.items(), key=operator.itemgetter(1), reverse=True))

    @staticmethod
    def _get_inverted_index(path):
        ii, _ = tokenization.create_inverted_list(path)
        return ii


if __name__ == '__main__':
    unigram_file_path = "../hw04/unigram_index.json"
    doc_count_file_path = ""
    corpus_path = '../hw03/corpus'

    # bm25_ranker = BM25(unigram_data, b=0.75, k1=1.2, k2=100)
    bm25_ranker = partial(bm25_scoring, unigram_file_path, doc_count_file_path)

    prf = PseudoRelevance(corpus_path, bm25_ranker, 10)
    prf.search("hurricane season")
