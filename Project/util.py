import pickle

# contain all utility functions

# serialize the directory
def save_and_serialize_content(file_path, file_path_serial, gram, dict):
   file_name_serial='../' + file_path_serial + gram
   with open(file_name_serial, "wb+") as file:
        pickle.dump(dict, file)
   file_name = '../'+file_path+gram
   with open(file_name, "wb+") as f:
       for key, value in dict.items():
           f.write(('['+key+']').encode('ascii', 'replace'))
           for doc_id, count in value.items():
               f.write((' ['+str(doc_id)+' '+str(count)+']').encode('ascii','replace'))
           f.write(('\n').encode('ascii','replace'))

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