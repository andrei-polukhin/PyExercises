tree = {
    'carnivora': {
        'canis': {
            'c.lupus': 'c.l.familiaris'
        },
        'felis': 'f.catus'
    }
}  # a nested datatype (dictionary in Python)

"""
However, building each branch of this dictionary will take
a lot of operations. Here is when __missing__ method will help.
"""


class Person(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


people = Person()
people["Teclado"]["Jose"] = "Salvatierra"
people["Teclado"]["Rolf"] = "Rolfend"
people["Apple"]["Steve"] = "Jobes"
print(people)

"""
Out:
{'Teclado': {'Jose': 'Salvatierra', 'Rolf': 'Rolfend'},
    'Apple': {'Steve': 'Jobes'}}
"""
