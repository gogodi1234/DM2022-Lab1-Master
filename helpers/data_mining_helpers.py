import nltk
import os

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')   # 去掉頭尾的\n\t，順序無關
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):      #sent_tokenize => 斷句
        for word in nltk.word_tokenize(d, language='english'):   #word_tokenize => 斷詞
            # filters here
            tokens.append(word)
    return tokens

def split_txt(filename):
    sentence = []
    score = []
    path = 'data'
    with open(os.path.join(path,filename), 'r', encoding = 'utf-8') as f:
        for line in iter(f):
            #print(line)
            l = line.split('\t')
            sentence.append(l[0].strip(' '))
            score.append(l[1].strip('\n'))
    return sentence, score

