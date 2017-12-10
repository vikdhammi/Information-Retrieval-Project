def tf_idf_scoring(unigram_path, doc_count_path, query,stopwords=None):
    unigram = retrieve_json_serialize_content(unigram_path)
    doc_word_count = retrieve_json_serialize_content(doc_count_path)
    tf_idf_score={}
    N=len(doc_word_count)
    if stopwords is None:
        stopwords = []
    for word in query.split():
        if word not in stopwords and word in unigram:
            doc_count= len(unigram[word])
            idf_score = math.log10(N/float(doc_count))
            for doc,freq in unigram[word].items():
                tf_score = float(freq)/doc_word_count[doc]
                if doc in tf_idf_score:
                    tf_idf_score[doc]+= tf_score*idf_score
                else:
                    tf_idf_score[doc] = tf_score * idf_score
    sorted_doc_score_list = sorted(tf_idf_score.items(), key=lambda doc: doc[1], reverse=True)[:100]
    return sorted_doc_score_list
