from __future__ import division

import os
from collections import defaultdict

from bs4 import BeautifulSoup


def calc_significance(sentence, query):
    query_set = {w for w in query.split()}

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


def get_sentences(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    text = soup.get('pre')
    sentences = [s.strip() for s in text.d if s.strip()]
    return sentences


def gen_snippet_for_query(query, file_path, max_sentences=3):
    sentences = get_sentences(file_path)

    # schema: significance_score1: [(sentence1, pos1), (sentence2, pos2)]
    #         significance_score2: [(sentence3, pos3)]
    # pos<x> is position of sentence in file or sentences list
    significance_dict = defaultdict(list)

    for pos, sentence in enumerate(sentences):
        sig_score = calc_significance(sentence, query)
        significance_dict[sig_score].append((sentence, pos))

    unsorted_snippets = []  # contains list of tuples of (sentence, pos)
    for score in sorted(significance_dict.keys()):
        unsorted_snippets.append(significance_dict[score])

        if len(unsorted_snippets) == max_sentences:
            break

    return sorted(unsorted_snippets, key=lambda s: s[1])


def write_snippets_to_file(f, snippets, docid, query):
    f.write("""<h3> Snippet from %s </h3></br>""" % docid)

    q_set = {w for w in query.split()}

    elems = ["<p>"]
    for snippet in snippets:
        for word in snippet:
            if word in q_set:
                elems.append("""<b>%s</b>""" % word)
            else:
                elems.append(word)

        elems.append("...")
    elems.append("</p>")

    f.write("".join(elems))
    f.write("</br></br>")


def generate_snippets(results_file, dump_path, output_dir):
    with open(results_file, 'r') as rf:
        entries = rf.readlines()

    query_id = entries[0].split(" ")[2]
    of = open(os.path.join(output_dir, query_id) + '.html')

    for entry in entries:
        parts = entry.split(" ")
        doc_id = parts[2]
        query = parts[1]

        file_path = os.path.join(dump_path, doc_id) + '.html'
        snippets = gen_snippet_for_query(query, file_path)

        write_snippets_to_file(of, snippets, doc_id, query)

    of.close()
