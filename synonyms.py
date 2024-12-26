'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    denominator = norm(vec1) * norm(vec2)
    n1 = list(vec1.keys())
    n2 = list(vec2.keys())
    num = 0
    for i in range(min(len(n1), len(n2))):
        if n1[i] in n2:
            num += vec1[n1[i]] * vec2[n1[i]]
    return(num/denominator)


def create_dict(sentence,word):
    d = dict()
    for e in sentence:
        if e.lower() != word.lower():
            d[e.lower()] = 1
    return d


def build_semantic_descriptors(sentences):
    semantic_discriptors = dict()
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j].lower() in semantic_discriptors.keys():
                for e in sentences[i] :
                    if e.lower() in semantic_discriptors[sentences[i][j].lower()]:
                        semantic_discriptors[sentences[i][j].lower()][e.lower()] += 1
                    elif e.lower() != sentences[i][j].lower():
                        semantic_discriptors[sentences[i][j].lower()][e.lower()] = 1
            else:
                semantic_discriptors[sentences[i][j].lower()] = create_dict(sentences[i],sentences[i][j].lower())
    return semantic_discriptors


def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for s in filenames:
        f = open(s,"r" ,encoding="latin1").read()
        f = f.replace("!" , ".")
        f = f.replace("?" , ".")
        f = f.replace("\n" , " ")
        f = f.split(".")
        for l in f:
            l = l.split()
            sentences.append(l)
    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similar = dict()
    for e in choices:
        if word in semantic_descriptors and e in semantic_descriptors:
            similar[e] = similarity_fn(semantic_descriptors[word], semantic_descriptors[e])
        else:
            similar[e] = -1
    maxim = [choices[0], similar[choices[0]]]
    for k in choices:
        if similar[k] > maxim[1]:
            maxim = [k , similar[k]]
    return maxim[0]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename,"r" ,encoding="latin1")
    line = f.readline()
    count = 0
    correct = 0
    while line  != "":
        words = line.split()
        check = most_similar_word(words[0],words[2:], semantic_descriptors, similarity_fn)
        count += 1
        if(check == words[1]):
            correct+= 1
        line = f.readline()
    return (correct / count)*100