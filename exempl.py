import json

#date={1:"www","number":"123-334-445"}


#with open('s.json','w', encoding ='utf-8')as file:
    #json.dump(date,file)


with open('s.json', 'r', encoding ='utf-8')as file:
     dd = json.load(file)
     #print(dd)

with open('s.json','w', encoding ='utf-8')as file:
    json.dump(date,file)