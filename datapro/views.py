from django.shortcuts import render
from .queryBoolean import *
from .synon import *
from .match import *
from .readDB import *
# import nltk

# Create your views here.
def home(request):
    return render(request,'home.html',{'db':db})

def description_search(request):
    query = request.GET['query1']
    q_processed=preProcessing(query)
    query=query.split()
    candidate=synonyms(query, q_processed)
    query_list=randomPick(candidate)
    avgResult = match(query_list)
    list = []
    db_list = []

    for item in range(5):
        list.append(avgResult[item][0])
        db_list.append(db[avgResult[item][0]])
    
    original_data = []
    for i in range(5):
        f = open('static/recipe.txt','rt',encoding ='UTF8')
        while True:
            line = f.readline()
            if not line: break
            data = line.split(';')
            data[2] = data[2].split('\\')
            data[4] = data[4].split('\\')
            data[5] = data[5].split(':')
            del data[5][0]
            
            for j in range(len(data[5])-1):
                data[5][j] = data[5][j].strip()
                data[5][j] = data[5][j][:-1]

            # data[7] = data[7].strip()
            if data[1].strip() in db_list[i]['name'].strip():
                original_data.append(data)
                print("yes")
        f.close()
    return render(request,'description_result.html',{'query':query,'avgResult':list,'db_list':db_list,'data':original_data})

def ingredient_search(request):
    query = request.GET['query2']
    candidate = FindN(query)
    NAdata_name = NA_Ingredient_nameonly(candidate, db) # 소팅되지 않은 해당 음식들 전부
    NAdata_all = NA_Ingredient_all(candidate, db) # 소팅되지 않은 음식들의 값 전부 계산
    NAdata = NA_Ingredient(candidate, db) # 소팅된 음식들의 weight 빼고
    NAdata_weight = NA_Ingredient_weight(candidate, db) # data에는 chicken과 onion이 포함된 커리만 출력됨 - ranking을 통해 5위까지 출력
    db_list = []

    for item in range(5):
        db_list.append(db[NAdata[item]])

    original_data = []
    for i in range(5):
        f = open('static/recipe.txt','rt',encoding ='UTF8')
        while True:
            line = f.readline()
            if not line: break
            data = line.split(';')
            data[2] = data[2].split('\\')
            data[4] = data[4].split('\\')
            data[5] = data[5].split(':')
            del data[5][0]
            
            for j in range(len(data[5])-1):
                data[5][j] = data[5][j].strip()
                data[5][j] = data[5][j][:-1]

            if data[1].strip() in db_list[i]['name'].strip():
                original_data.append(data)
                print("yes")
        f.close()
    return render(request,'ingredient_result.html',{'data':original_data,'db_list':db_list,'query':query,'candidate':candidate,'NAdata_name':NAdata_name,'NAdata_all':NAdata_all,'NAdata':NAdata,'NAdata_weight':NAdata_weight})