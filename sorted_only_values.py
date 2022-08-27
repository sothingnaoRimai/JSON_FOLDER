#  convert python dict to json data
# {
#    "6": 5,
#    "9": 9,
#    "2": 10
# }
import json
a={'9':5,'6':10,'2':9}
b=sorted(a.values())
dict={}
for i in b:
    for k in a.keys():
        if a[k]==i:
            dict[k]=a[k]
a=open("sort_values","w")
json.dump(dict,a,indent=3)

