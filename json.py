import json

people_string = '''
{
    "people": [
    {
        "name": "Ashley",
        "email": "ash@email.co.uk"
    },
    {
        "name": "Phil",
        "email": "phil@email.com"
    },
    {
        "name": "Joe",
        "email": "joe@email.co.uk"
    }
    ]
}
'''

data = json.loads(people_string)

print(type(data['people']))
print()

for person in data['people']:
    #print(person['name'])
    del person['name']