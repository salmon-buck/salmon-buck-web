from .synon import *
import operator

def match(query_list):
    alpha=50
    totalResult=[]
    t=1e-5
    rank=5
    for query in query_list :
        result={}
        for food in smoothing_prob.keys():
            r=1
            for term in query :
                if term in smoothing_prob[food].keys() :                    # 해당요리에 있는경우
                    r *= smoothing_prob[food][term]
                elif term in collection_prob :                              # 해당요리에 없고 전체 corpus에 존재하는경우
                    r *= (alpha*collection_prob[term]) / (len(smoothing_prob[food]) + alpha)
                else :                                                      # 동의어까지 돌렸는데 찾을수 없는경우(오타일 경우포함)
                    r *= (alpha*t) / (len(smoothing_prob[food]) + alpha)
            result[food]=r
        sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
        totalResult.append(sorted_result)

    avgResult=dict()
    for i in range(len(query_list)) :
        cnt = 1
        for (doc, sim) in totalResult[i]:
            if doc in avgResult.keys() :
                avgResult[doc]+=sim
            else :
                avgResult[doc]=sim

    for v in avgResult.keys() :
        avgResult[v] /=len(query_list)

    avgResult = sorted(avgResult.items(), key=operator.itemgetter(1), reverse=True)

    cnt=1
    return avgResult
    # for (doc, sim) in avgResult :
    #     print(str(cnt) + ". " + doc + " :" + str(sim))
    #     if cnt>=rank :
    #         break
    #     cnt += 1

'''
for i in range(len(query_list)) :
    print("<query{} : ".format(i+1), ' '.join(query_list[i]), " >")
    cnt=1
    for (doc, sim) in totalResult[i] :
        print(str(cnt) + ". " + doc + " :" + str(sim))
        if cnt>=rank :
            break
        cnt += 1
    print()
'''