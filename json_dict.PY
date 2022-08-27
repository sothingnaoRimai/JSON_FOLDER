# # # Write a program to convert json data into python objects

import json

# loads:json string to dictonary object
a='{"name":"soso","age":true,"car":null}'
d=json.loads(a)
print(d)