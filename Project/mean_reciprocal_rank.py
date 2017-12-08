import os
from operator import itemgetter
from __future__ import division
import system_evaluation

def find_mean_reciprocal_rank(file, relevant, model_docs):
    rank = 0
    id = 1
    while id != (len(model_docs) + 1):
        if str(id) not in relevant:
            id = id + 1
            rank = rank
            continue

        models_list = model_docs[str(id)]
        r_docs = relevant[str(id)]

        for each in models_list:
            position = each.split()[3]
            docNo = each.split()[2]
            flag = False
            for every in r_docs:
                if (docNo == every.split()[2]):
                    flag = True
                    rank = rank + 1 / position
                    break
            if flag:
                break
        id = id + 1
    mrr = rank / len(model_docs)

