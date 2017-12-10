from __future__ import division
import sys
import os
import glob
import string
import math
import operator
from pathlib import Path
from collections import Counter
import util


def query_smoothing(unigram_path, doc_count_path, query):
    invertIndex = util.retrieve_json_serialize_content(unigram_path)
    totalWords = util.retrieve_json_serialize_content(doc_count_path)
    queryTermDict = {}
    queryLikelihood = {}
    tokenSum = 0
    alpha_d = 0.35
    for s in totalWords.values():
        tokenSum += s
    tokens = tokenSum
    totalDocs = totalWords.items()

    # qyList = open('query.txt', 'r')
    # for row in qyList.readlines():
    #     queryWords = row.split(' ')
    #     query = ' '.join(queryWords[1:])[:-1].lower()
    #     qid = queryWords[0]

    queryLine = query.split(' ')
    for each in queryLine:
        if each not in queryTermDict:
            queryTermDict[each] = 1
        else:
            queryTermDict[each] += 1

        score = 0
        word_count = 0
        for word in queryTermDict:

            if word in invertIndex:
                doc_list = invertIndex[word]
                corpus_freq = 0

                for doc in doc_list:

                    f_q = invertIndex[word][doc]
                    for every in doc_list:
                        corpus_freq += doc_list[every]
                    # if word in wordLen:
                    #     word_count = wordLen[word]

                    t1 = (1 - alpha_d) * (f_q / totalWords[doc])
                    t2 = alpha_d * (corpus_freq / tokens)

                    score = t1 + t2

                    queryLikelihood[doc] = score

        sortedQueryTermDict = sorted(queryLikelihood.items(), key=operator.itemgetter(1), reverse=True)
        return sortedQueryTermDict
