import pickle
import json
import os
# contain all utility functions

# serialize the directory
def save_json_serialize_content(file_path_serial,file_name, dict):

   with open(os.path.join(file_path_serial,), "w") as file:
        file.write(json.dumps(dict))
   # file_name = '../'+file_path+gram
   # with open(file_name, "wb+") as f:
   #     for key, value in dict.items():
   #         f.write(('['+key+']').encode('ascii', 'replace'))
   #         for doc_id, count in value.items():
   #             f.write((' ['+str(doc_id)+' '+str(count)+']').encode('ascii','replace'))
   #         f.write(('\n').encode('ascii','replace'))

def retrieve_json_serialize_content(file_path_serial):
   with open(os.path.join(file_path_serial), "r") as f:
        dict_unigram=json.load(f)
   return dict_unigram
# derserialize the directory
def retrieve_dicitionary_content_deserialize(file_name):
    with open(file_name, "rb") as file:
        dict=pickle.load(file)
    return dict

# save content of the list
def save_list_content(file_name,list):
    f = open( file_name , 'wb+')

    for value in list:
        f.write(('['+value[0]+']'+' ['+str(value[1])+']\n').encode('ascii','replace'))
    f.close()

# save doc frequency list
def save_docfreq_list_content(file_name,list):
    f = open( file_name, 'wb+')
    for value in list:
        f.write(('['+value[0]+']'+' '+str(value[1][0])+' ['+str(value[1][1])+']\n').encode('ascii','replace'))
    f.close()

# deserialize the directory file
def retrieve_list_content(file_name):
    with open(file_name, "rb") as file:
        dict=pickle.load(file,)
    return dict

# save content in dictionary
def save_dicitionary_content(file_name, dict ):
    f = open(file_name, 'wb+')
    for key, value in dict.items():
        f.write(key.encode('ascii','replace'))
        f.write((" ["+str(value)+']\n').encode('ascii','replace'))
    f.close()

def save_html_content(url, text):
        f = open(url + '.txt', 'w')
        f.write(text)
        f.close()

