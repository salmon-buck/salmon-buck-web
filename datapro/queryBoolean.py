from .readDB import *
from .preProcessing import preProcessing
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
import operator


def fn_nvarFilt(poses, nvar):
    nvjr = list(nvar)
    ja = lambda tag: tag if tag != 'j' else 'a'
    nvars = [(p0, ja(p1[:1].lower())) for p0, p1 in poses if p1[:1] in nvjr]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(nvar[0], pos=nvar[1]) for nvar in nvars]

def FindN(query):
    tokens = word_tokenize(query.lower())
    poses = pos_tag(tokens)
    nltk_res = fn_nvarFilt(poses, 'N')
    nltk_freq = defaultdict(int)
    for token in nltk_res:
        nltk_freq[token] += 1
    return nltk_res

# FindN 을 사용하여 쿼리에서 명사를 추출하여 Boolean에 사용

# q=input() #쿼리 입력 ex) warm chicken with onion

# candidate=FindN(q)   # candidate = [chicken,onion]

### 이 경우는 무조건 쿼리에 적힌 재료들이 포함되어 있는 경우, 
###예를들어 양파 닭 소금이 쿼리에 있다면 저 3개를 모두 가지고 있는 결과물 중에서 검색

def boolean_Ingredient_all(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu not in s:
                break;
            else:
                flag += 1 
        if flag == len(q_ing):
            querylen =len(q_ing)
            inglen=len(s.split(' '))
            rank_value = querylen/inglen
            lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    return lg

def boolean_Ingredient_nameonly(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu not in s:
                break;
            else:
                flag += 1 
        if flag == len(q_ing):
            querylen =len(q_ing)
            inglen=len(s.split(' '))
            rank_value = querylen/inglen
            lg.append(food)
    return lg

def boolean_Ingredient(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu not in s:
                break;
            else:
                flag += 1 
        if flag == len(q_ing):
            querylen =len(q_ing)
            inglen=len(s.split(' '))
            rank_value = querylen/inglen
            lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    for i in range(5):
        if (len(lg)-i-1) == -1:
            break;
        
        ranked.append(lg[len(lg)-1-i][0])
        
    return ranked

def boolean_Ingredient_weight(q_ing, db_ing) :
    ranked_with_weight = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu not in s:
                break;
            else:
                flag += 1 
        if flag == len(q_ing):
            querylen =len(q_ing)
            inglen=len(s.split(' '))
            rank_value = querylen/inglen
            lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    for i in range(5):
        if (len(lg)-i-1) == -1:
            break;
        ranked_with_weight.append(lg[len(lg)-i-1])
        
    return ranked_with_weight
# data_name = boolean_Ingredient_nameonly(candidate, db) # 소팅되지 않은 해당 음식들 전부
# data_all = boolean_Ingredient_all(candidate, db) # 소팅되지 않은 음식들의 값 전부 계산
# data = boolean_Ingredient(candidate, db) # 소팅된 음식들의 weight 빼고
# data_weight = boolean_Ingredient_weight(candidate, db) # data에는 chicken과 onion이 포함된 커리만 출력됨 - ranking을 통해 5위까지 출력
# print(data_name)
# print(data_all)
# print(data)
# print(data_weight)

### 이 경우는 쿼리에 적힌 재료들이 모두 포함되어 있지 않더라도 가까운 경우, 
###예를들어 양파 닭 소금이 쿼리에 있다면 저 2개만을 가지고 있더라도 가까운 음식 중에서 검색

def NA_Ingredient_all(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu in s:
                flag +=1

        flaglen = flag
        inglen=len(s.split(' '))
        rank_value = flaglen/inglen
        lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    return lg

def NA_Ingredient_nameonly(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu in s:
                flag +=1
        flaglen =flag
        inglen=len(s.split(' '))
        rank_value = flaglen/inglen
        lg.append(food)
    return lg

def NA_Ingredient(q_ing, db_ing) :
    ranked = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu in s:
                flag +=1
        flaglen = flag
        inglen=len(s.split(' '))
        rank_value = flaglen/inglen
        lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    
    for i in range(5):
        if (len(lg)-i-1) == -1:
            break;
        ranked.append(lg[len(lg)-1-i][0])
        
    return ranked

def NA_Ingredient_weight(q_ing, db_ing) :
    ranked_with_weight = []
    lg =[]
    for food in db.keys():
        flag = 0
        s = db[food]['ingredient']
        for qu in (q_ing):
            if qu in s:
                flag+=1;
                
        flaglen = flag
        inglen=len(s.split(' '))
        rank_value = flaglen/inglen
        lg.append([food, rank_value])
    
    lg =sorted(lg, key=operator.itemgetter(1))
    for i in range(5):
        if (len(lg)-i-1) == -1:
            break;
        ranked_with_weight.append(lg[len(lg)-i-1])
        
    return ranked_with_weight
# NAdata_name = NA_Ingredient_nameonly(candidate, db) # 소팅되지 않은 해당 음식들 전부
# NAdata_all = NA_Ingredient_all(candidate, db) # 소팅되지 않은 음식들의 값 전부 계산
# NAdata = NA_Ingredient(candidate, db) # 소팅된 음식들의 weight 빼고
# NAdata_weight = NA_Ingredient_weight(candidate, db) # data에는 chicken과 onion이 포함된 커리만 출력됨 - ranking을 통해 5위까지 출력
# print(NAdata_name)
# print(NAdata_all)
# print(NAdata)
# print(NAdata_weight)

