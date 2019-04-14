import json

#SAMPLE
userJSON = '{"first_name":"John","last_name":"Doe","age":30}'

#Parse to Dictionary
user = json.loads(userJSON)
#print(user)
#print(user['first_name'])

car = {'make':'Ford','model':'Mustang','year':'1967'}
carJSON = json.dumps(car)

print(carJSON)