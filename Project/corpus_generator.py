import glob
import os
import re
import sys
from bs4 import BeautifulSoup
import util

# driver function to run clean corpus generation
# def main(argv):
#     input_path,output_path, serialized_output_path=argv
#     generate_corpus(input_path,output_path,True,True)

# generates clean output and writes in provided output path
def generate_corpus():
    input_path = 'Cacm'
    output_path = 'Processed_Docs'
    os.chdir(input_path)
    for file in glob.glob('*.html'):
        raw_content = open(file,encoding='ascii').read()
        data = BeautifulSoup(raw_content,'html.parser')
        fileName = file.strip('.html')
        content = data.find('pre')
        # content=remove_tags(content)
        content_text = content.get_text()
        content_text = remove_punctuation(content_text)
        content_text=content_text.lower()
        content_text=content_cleaning(content_text)
        # util.save_html_content('../'+output_path+file[:-4],content_text.encode('ascii','replace'))
        util.save_html_content('../' + output_path +'/'+ fileName, content_text)
    os.chdir('..')

# cleaning content including spaces and unreadable character
def content_cleaning(content):
    # remove url
    content = re.sub(r'http\S+', ' ', content)
    # remove unreadable character
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)

    # dealing with spaces
    # remove end and trail space in line
    filter=''
    for line in content.split('\n'):
        line.strip()
        for word in line.split(" "):
            word=word.strip().replace('\t','')
            if(word!=''):
                filter+=(' '+word)
    filter=filter.strip()
    return filter

# remove unwanted tags
def remove_tags(content):
    for tag in content.findAll("sup", {"class": ["reference"]}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "References"}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "External_links"}):
        tag.decompose()
    for tag in content.findAll(['style', 'script', 'sup', 'sub']):
        tag.decompose()
    for tag in content.findAll("span", {"class": ["mw-editsection", "mwe-math-element"]}):
        tag.decompose()
    for tag in content.findAll("div", {"id": "toc"}):
        tag.decompose()
    for tag in content.findAll("div", {"class": "reflist"}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "Further_reading"}):
        tag.decompose()
    for tag in content.findAll("table", {"class": "plainlinks"}):
        tag.decompose()
    for tag in content.findAll("a"):
        tag.decompose()
    for tag in content.findAll("div", {"class": ["catlinks"]}):
        tag.decompose()
    return content

# remove all punctuation
def remove_punctuation(content):
    content = re.sub(r"[[\\\]:;<=>!\"_`{|@^}~$%&\'()#*+/?]", " ", content)
    # remove - on basis of regex checking before and after check in between words and numerals
    content = re.sub(r"(?<![0-9A-Za-z])-|-(?![0-9A-Za-z])", " ", content)
    # remove ',' and '.' but not from between digits
    content = re.sub(r"(?<![0-9])[,.]|[,.](?![0-9])", " ", content)
    return content

# if __name__=='__main__':
#     main(sys.argv[1:])