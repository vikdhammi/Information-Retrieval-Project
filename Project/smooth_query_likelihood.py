from __future__ import division
import sys
import os
import glob
import string
import math
import operator
from pathlib import Path
from collections import Counter

class Smoothing:

     #def query_likelihood(self):
        invertIndex = {}
        totalWords = {}
        docContent = {}
        queryTermDict = {}
        queryLikelihood = {}
        totalDocNo = 1000
        tokenSum = 0
        alpha_d = 0.35
        path = 'Test'
        os.chdir(path)
        # files = [f for f in os.listdir(path) if f .endswith('.txt')]
        files = glob.glob('*.txt')
        counter = 0
        print(len(files))

        wordLen = Counter()
        for file in files:
            # with open(file, 'r') as f:
            f = open(file)
            doc = f.read()
            content = doc.split()
            docNO = str(file).split("~")[1].replace(".txt", "")
            totalWords[docNO] = len(content)
            docContent[docNO] = content
            # print(docNO)
            # print(doc)

            for words in content:
                wordLen[words] += 1
                if not (words in invertIndex):
                    invertIndex[words] = {docNO: 1}
                else:
                    value = invertIndex[words]
                    if not (docNO in value):
                        invertIndex[words].update({docNO: 1})
                    else:
                        value[docNO] += 1
            f.close()

        for k, v in invertIndex.items():
            print(k, v)

        os.chdir("..")

        

        for s in totalWords.values():
            tokenSum += s
        tokens = tokenSum
        totalDocs = totalWords.items()

        qyList = open('query.txt', 'r')
        for row in qyList.readlines():
            queryWords = row.split(' ')
            query = ' '.join(queryWords[1:])[:-1].lower()
            qid = queryWords[0]

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

            qid = queryWords[0]

            ouputFile = open(qid + '_QueryLikelihood_List.txt', 'w')
            for indexer in range(min(len(sortedQueryTermDict), 100)):
                position = indexer + 1
                ouputFile.write(
                        str(qid) + ' Q0 ' + str(sortedQueryTermDict[indexer][0]) + ' '+ str(position) + ' ' + 'Score=' +
                        str(sortedQueryTermDict[indexer][1]) + ' '
                        + 'Query Likelihood' + '\n')

            ouputFile.close()