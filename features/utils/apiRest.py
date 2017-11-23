import requests
from features.utils.file_system import *

data = FileSystem('../data/data_user.json')

header = {'Authorization':'Basic cWEudGVzdGluZy5kZ3NAZ21haWwuY29tOmRpZWdvMTk4Nw=='}
r = requests.get('https://todo.ly/api/user.json', headers=header)

result = r.json()
#print(result['Id'])
#print(result['Email'])

print(data._get_DataJson())


op1 = data._get_DataJson()
print(data._compare_to(op1, r.json()))
data._print_structure_json(op1)

data._cleanup()