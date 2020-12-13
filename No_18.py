import json

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_string = '{"name": "Allen", "age": 21}'

person_dict = json.loads(person_string)
print(person_dict)
person_object = Person(**person_dict)
print(person_object.name)
