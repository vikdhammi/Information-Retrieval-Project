from __future__ import division

import json
import os

from bs4 import BeautifulSoup
from collections import defaultdict

from hw04.bm25_index import BM25


class SnippetGenerator(object):
    def __init__(self, ranker, unigram_index, dump_path):
        self.unigram_index = unigram_index
        self.dump_path = dump_path
        self.ranker = ranker

    def search(self, query, max_sentences=3):
        top_results = self.ranker.search_index(query, max_hits=10)
        for docid, score in top_results.iteritems():
            snippet = self._gen_snippet_for_term(docid, query, max_sentences)

    def _gen_snippet_for_term(self, docid, query, max_sentences):
        file_path = os.path.join(self.dump_path, docid) + '.html'
        sentences = self._get_sentences(file_path)

        # schema: significance_score1: [(sentence1, pos1), (sentence2, pos2)]
        #         significance_score2: [(sentence3, pos3)]
        # pos<x> is position of sentence in file or sentences list
        significance_dict = defaultdict(list)

        for pos, sentence in enumerate(sentences):
            sig_score = self._calc_significance(sentence, query)
            significance_dict[sig_score].append((sentence, pos))

        unsorted_snippets = []  # contains list of tuples of (sentence, pos)
        for score in sorted(significance_dict.keys()):
            unsorted_snippets.append(significance_dict[score])

            if len(unsorted_snippets) == max_sentences:
                break

        snippet = "...".join(sorted(unsorted_snippets, key=lambda s: s[1]))

        return snippet

    def _get_sentences(self, file_path):
        with open(file_path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

        text = soup.get('pre')
        sentences = [s.strip() for s in text.d if s.strip()]
        return sentences

    def _calc_significance(self, sentence, query):
        query_set = set(query)

        words = sentence.split()
        start_pos = None
        end_pos = None
        sig_terms = 0

        # get first occurance
        for pos, word in enumerate(words):
            if word in query_set:
                if start_pos is None:
                    start_pos = pos

                end_pos = pos
                sig_terms += 1

        if (start_pos is None) or (start_pos - end_pos) == 0:
            return 0

        return (sig_terms ** 2) / (start_pos - end_pos)


if __name__ == '__main__':
    unigram_file_path = "../hw04/unigram_index.json"
    unigram_data = json.load(open(unigram_file_path, 'r'))
    corpus_path = '../hw03/corpus'

    bm25_ranker = BM25(unigram_data, b=0.75, k1=1.2, k2=100)

    sg = SnippetGenerator(corpus_path, bm25_ranker)
    sg.search("hurricane disaster")
