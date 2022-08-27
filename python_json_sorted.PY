# #  write a program to convert python object to string 
# #sorted# store in json file by using dump
import json
a={'9':5,'2':3,'13':8}
b=sorted(a.values())
c={}
for i in b:
    for x in a.keys():
        if a[x]==i:
            c[x]=a[x]
a=open("key_value_sort","w")
json.dump(c,a,indent=3)
print(a)
