import glob
import os
import sys
import util

# driver function to perform statistical tokenization
def create_indexer():
    input_path = 'Processed_Docs'
    output_path='Corpus Stats'
    os.chdir(input_path)
    for file in glob.glob('*'):
        input_dict = util.retrieve_dicitionary_content_deserialize(file)
        freq_sorted_tf_dict=term_frequency(input_path)
        lexograph_df_dict=doc_frequency(input_path)
        util.save_list_content('../'+output_path+'/'+'_termfreq',freq_sorted_tf_dict)
        util.save_docfreq_list_content('../'+output_path+'/' + '_docfreq',lexograph_df_dict)

# finding term frequency
def term_frequency(input):
    tf_dict = {}
    for token,value in input.items():
        freq=0
        for key, count in value.items():
            freq+=count
        tf_dict[token]=freq
    # sorting on the basis of frequency
    freq_sorted_tf_dict=sorted(tf_dict.items(), key=lambda x : x[1], reverse=True)
    return freq_sorted_tf_dict

# finding document frequency
def doc_frequency(input):
    df_dict={}
    for token,value in input.items():
        doc_id = []
        doc_freq=0
        for key,count  in value.items():
            doc_id.append(key)
            doc_freq+=1
        df_dict[token]=(doc_id,doc_freq)
    # sorting lexographically
    lexograph_dict=sorted(df_dict.items(), key=lambda x: x[0])
    return lexograph_dict

# if __name__=='__main__':
#     main(sys.argv[1:])