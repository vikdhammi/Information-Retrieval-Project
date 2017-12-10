import glob
import os
import sys
import util

# driver function to provide tokenized output
def main(argv):
    input_path,output_path=argv
    unigram, doc_count = create_inverted_list(input_path)

    util.save_json_serialize_content(output_path, 'indexed_output.json', unigram)
    util.save_json_serialize_content(output_path, 'doc_word_count.json', doc_count)


# inverted index creation and saving at output path
def create_inverted_list(input_path):
    # output_path = 'Unigram'
    # serialized_output_path = 'Serialized_Output'

    doc_word_count = {}
    unigram = {}

    if isinstance(input_path, str):
        file_list = [input_path]  # input_path is a path to single file

    else:
        file_list = [os.path.join(input_path, f) for f in os.listdir(input_path)]

    for file in file_list:
        content = open(file, encoding='utf-8').read()
        doc_name = file.split()[0]
        docId = doc_name.split(".")[0]
        words = content.split()
        words_len = len(words)
        doc_word_count[docId] = words_len
        count = 0
        for i in range(len(words)):
            word = words[i]
            # unigram
            if word in unigram:
                value = unigram[word]
                if docId in value:
                    value[docId] += 1
                else:
                    unigram[word].update({docId: 1})
            else:
                unigram[word] = {docId: 1}
                count += 1


    return unigram, doc_word_count
    #
    # util.save_json_serialize_content(output_path,'indexed_output.json', unigram)
    # util.save_json_serialize_content(output_path,'doc_word_count.json', doc_word_count)

    # doc_token_count = {}
    # unigram={}
    # for file in os.listdir(input_path):
    #     content = open(os.path.join(input_path,file),encoding='utf-8').read()
    #     docId = str(file).split(".")[0]
    #     words = content.split()
    #     words_len = len(words)
    #     count=0
    #     for i in range(len(words)):
    #         word = words[i]
    #         #unigram
    #         if word in unigram:
    #             value = unigram[word]
    #             if docId in value:
    #                 value[docId]+=1
    #             else:
    #                 unigram[word].update({docId:1})
    #         else:
    #             unigram[word]={docId:1}
    #             count += 1
    #
    #     doc_token_count[docId] = count
    #
    # print(unigram)
    # # saving content at output path
    # util.save_json_serialize_content(output_path,unigram)
    # # util.save_dicitionary_content('../'+output_path+'/document_tokenization.txt',doc_token_count)


if __name__=='__main__':
    main(sys.argv[1:])