import json
a=["NEELAM","PROGRAMMER","24","2000"]
b=["NIDHI","TRAINER","29","30000"]
c=["ANURAG","HR","28","50000"]
d=["ABHISHEK","MANAGER","25","64000"]
list=[a,b,c,d]
out_key=["emp1","emp2","emp3","emp4"]
key_in=["Name","Disignation","Age","Salary"]
dict={}
i=0
while i<len(list):
    j=0
    dict1={}
    while j<len(list[i]):
        dict1[key_in[j]]=list[i][j]
        j=j+1
    dict[out_key[i]]=dict1
    i=i+1
with open("list_dict.json","w") as f:
    json.dump(dict,f,indent=3)