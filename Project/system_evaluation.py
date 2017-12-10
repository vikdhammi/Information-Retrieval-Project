import os
from operator import itemgetter
from __future__ import division
import precision_at_k
import mean_reciprocal_rank

def main():
    relevant = {}
    model_docs = {}
    recall = {}
    precision = {}
    relevant = find_relevant_docs()
    model_docs = find_ranked_model_docs()
    mean_reciprocal_rank.find_mean_reciprocal_rank(file, relevant, model_docs)
    find_precision_recall(file, relevant, model_docs)
    precision_at_k.find_precision_at_k(file, relevant, model_docs)


def find_ranked_model_docs():
    model_docs = {}
    ranked_docs = open('BM25.txt','r')
    for each in  ranked_docs.readlines():
        line = each.split()

        if model_docs.has_key(line[0]):
            text = model_docs.get(line[0])
            text.append(each[:-1])
        else:
            model_docs[line[0]] = [each[:-1]]
    ranked_docs.close()
    return model_docs

def find_relevant_docs():
    relevant = {}
    list_of_relevant_docs = open('Given_files/'+'cacm.rel.txt','r')

    for doc in list_of_relevant_docs.readlines():
        line = doc.split()

        if relevant.has_key(line[0]):
            text = relevant[line[0]]
            text.append(doc[:-1])
        else:
            relevant[line[0]] = [doc[:-1]]
    list_of_relevant_docs.close()
    return relevant

def find_precision_recall(file, relevant, model_docs):
    avg_precision_queries = 0
    precision = {}
    recall = {}

    pr_file = open('Task1/'+'BM25.txt','w')
    queries = len(model_docs) + 1
    for each in range(1, queries):
        sum = 0
        discovered_docs = 0
        avg_precision = 0
        count = 0
        if str(each) not in relevant:
            precision[str(each)] = []
            recall[str(each)] = []
            continue
        precision[str(each)] = []
        recall[str(each)] = []
        r_docs = relevant[str(each)]

        for every in model_docs:
            count = count + 1
            flag = False
            id = every.split()[2]
            position = every.split()[3]
            score = every.split()[4]
            for doc in r_docs:
                if (id == every.split()[2]):
                    flag = True
                    break

            if not flag:
                # for Non relevant docs
                recall_val = discovered_docs / len(r_docs)
                precision_val = discovered_docs / count
                recall[str(each)].append({id: recall_val})
                precision[str(each)].append({id: precision_val})
                pr_file.write()             # Need to fill the output file format
            else:
                # for Relevant docs
                discovered_docs = discovered_docs + 1
                recall_val =  discovered_docs / len(r_docs)
                precision_val = discovered_docs / count
                sum = sum + precision_val
                recall[str(each)].append({id: recall_val})
                precision[str(each)].append({id: precision_val})
                pr_file.write()              # Need to complete

        if (discovered_docs == 0):
            avg_precision = 0
        else:
            avg_precision = avg_precision + (sum / discovered_docs)

        # output avg_precison req?

        avg_precision_queries = avg_precision_queries + avg_precision
    mean_avg_prc = avg_precision_queries / len(model_docs)

    pr_file.close()
