from .readDB import *
from nltk.corpus import wordnet
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from .preProcessing import preProcessing

import random

def synonyms(query, query_processed) :
    candidate = [[] for i in range(len(query_processed))]
    count=0
    for w in query:
        w=preProcessing(w)
        if not w:
            continue

        w=w[0]
        if w not in collection_prob.keys() :
            for syn in wordnet.synsets(query[count]):
                for l in syn.lemmas():

                    if preProcessing(l.name())[0] in collection_prob.keys() :

                        candidate[count].append(preProcessing(l.name())[0])

        else :
            candidate[count].append(w)

        if not candidate[count]:
            candidate[count].append(w)

        count+=1

    return candidate

def randomPick(candidate) :
    query_list=[]
    itr=10
    mul=1
    for c in candidate :
        mul*=len(c)
    if mul<10 :
        itr=mul
    itr=10
    for i in range(itr) :
        query=[]
        for synonyms in candidate :
            tmp=random.choice(synonyms)
            query.append(tmp)
        query_list.append(query)

    return query_list

# q=input('검색 입력 : ')
# q_processed=preProcessing(q)
# q=q.split()
# candidate=synonyms(q, q_processed)
# print(candidate)
# query_list=randomPick(candidate)
# print(query_list)