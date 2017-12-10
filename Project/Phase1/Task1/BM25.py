# bm25 scoring function

import util
import math

def bm25_scoring(unigram_path, doc_count_path, query):
    unigram = util.retrieve_json_serialize_content(unigram_path)
    doc_word_count = util.retrieve_json_serialize_content(doc_count_path)
    query_freq_count = {}
    doc_score_dic = {}
    # provided constants
    k1=1.2
    b=0.75
    k2=100

    #finding frequnecy of query terms
    for word in query.split():
        if word in query_freq_count:
            query_freq_count[word]+=1
        else:
            query_freq_count[word]=1

    doc_count=len(doc_word_count)
    # average document length
    avdl = float(sum(doc_word_count.values()))/doc_count

    # traversing on each document to evaluate its score
    for doc in doc_word_count:
        word_count = doc_word_count[doc]
        K = k1 * ((1 - b) + (b * (word_count / avdl)))
        doc_score = 0
        for word in  query_freq_count:
            if word in unigram:
                # number of documents containing term
                ni= len(unigram[word])
                word_doc = unigram[word]
                qfi = query_freq_count[word]
                if doc in word_doc:
                    # term frequency in the document
                    fi = word_doc[doc]
                    constant_term_1 = (((k1 + 1) * fi) / (K + fi))
                    constant_term_2 = (((k2 + 1) * qfi) / (k2 + qfi))
                    value = math.log((float(doc_count-ni+0.5)/(ni+0.5)))
                    doc_score+=(value*constant_term_1*constant_term_2)
        # if document do not contain single query it won't be considered
        if(doc_score!=0):
            doc_score_dic[doc]=doc_score

    # finding top 100 scoring documents
    sorted_doc_score_list = sorted(doc_score_dic.items(), key = lambda doc : doc[1],reverse=True)[:100]
    return sorted_doc_score_list
