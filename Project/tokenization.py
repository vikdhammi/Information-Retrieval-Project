import glob
import os
import sys
import util

# driver function to provide tokenized output
# def main(argv):
#     input_path,output_path, serialized_output_path=argv
#     create_inverted_list(input_path,output_path,serialized_output_path)

# inverted index creation and saving at output path
def create_inverted_list():
    input_path = 'Processed_Docs'
    # output_path = 'Unigram'
    # serialized_output_path = 'Serialized_Output'
    doc_token_count = {}
    unigram={}
    print(os.getcwd())
    os.chdir(input_path)
    for file in glob.glob('*'):
        content = open(file,encoding='utf-8').read()
        docId = str(file).split(".")[0]
        words = content.split()
        words_len = len(words)
        count=0
        for i in range(len(words)):
            word = words[i]
            #unigram
            if word in unigram:
                value = unigram[word]
                if docId in value:
                    value[docId]+=1
                else:
                    unigram[word].update({docId:1})
            else:
                unigram[word]={docId:1}
                count += 1

        doc_token_count[docId] = count

    print(unigram)
    return unigram
    # saving content at output path
    # util.save_and_serialize_content(output_path,serialized_output_path,'/unigram.txt',unigram)
    # util.save_dicitionary_content('../'+output_path+'/document_tokenization.txt',doc_token_count)

#
# if __name__=='__main__':
#     main(sys.argv[1:])