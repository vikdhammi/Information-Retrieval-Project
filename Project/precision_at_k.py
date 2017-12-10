import os
from operator import itemgetter
from __future__ import division
import system_evaluation

def find_precision_at_k(file, relevant, model_docs):
    p_at_5 = {}
    p_at_20 = {}
    id = 1
    doc_count = len(model_docs) + 1

    while id != doc_count:
        if not relevant.get(str(id)):
            p_at_5[id] = 0.0
            p_at_20[id] = 0.0
            id = id + 1
            continue

        r_docs = relevant[str(id)]
        p_at_20[id] = find_p_at_20(r_docs, model_docs[str(id)[:20]])
        p_at_5[id] = find_p_at_5(r_docs, model_docs[str(id)[:5]])

        id = id + 1

    for k,v in p_at_20:
        print(k,v)

    for k, v in p_at_5:
        print(k,v)



def find_p_at_20(r_docs, top_list):
    cntr = 0
    for each in top_list:
        for doc in r_docs:
            if each.split()[2] == doc.split()[2]:
                cntr = cntr + 1

    return cntr / 20

def find_p_at_5(r_docs, top_list):
    cntr = 0
    for each in top_list:
        for doc in r_docs:
            if each.split()[2] == doc.split()[2]:
                cntr = cntr + 1

    return cntr / 5
