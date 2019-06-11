#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def dcg_at_k(r, k, method=0):
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0


# In[4]:


def ndcg_at_k(r, k, method=0):
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max


# In[5]:


def find_rel(answer, query, answer_rel):
    rels = np.zeros((len(query)))
    for i in range(len(query)):
        if query[i] in answer:
            index = answer.index(query[i])
            rels[i] = answer_rel[index]
    
    return rels


# In[6]:


answer = ['Korean Curry', 'Asian Style Nachos', 'Sesame Chicken Potstickers', 'Slow Cooker Corn Chowder', 'Instant Pot Mushroom Risotto']
query = ['Korean Curry', 'Sesame Chicken Potstickers', 'Easy Chicken Tikka Masala', 'Asian Style Nachos', 'Instant Pot Mushroom Risotto']

answer_rel = [5,4,3,2,1]

rel = find_rel(answer, query, answer_rel)
print(ndcg_at_k(rel, 5, 1))

