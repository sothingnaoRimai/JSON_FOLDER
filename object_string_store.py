# # convert python object to json string and dump/
# # store in a file(store string/json file)
import json
a={'name':'soso','age':23,'car':None}
b=json.dumps(a)
# print(b)
with open("object_string","w") as dict:
    json.dump(a,dict,indent=3)
    


