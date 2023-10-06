import json

data = {
    'key': 'my name',
    'another_key': [55, 'I am fine'],
    'more_key': True,
}

json_string = json.dumps(data)
print(json_string)

data_from_json = json.loads(json_string)
print(data_from_json)

with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

with open('data.json') as file:
    data_ = json.load(file)
    print(data_)
