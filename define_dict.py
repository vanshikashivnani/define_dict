# empty dictionary
d = {}

d = dict()  # same thing

d = {1: 'one', 2: 'two'}
print(d)

eng_to_spa = {'hello': 'hola', 'yes': 'sí', 'dictionary': 'diccionario', 'one': 'uno', 'two': 'dos', 'no': 'no'}
print(eng_to_spa), len(eng_to_spa)
print(f'two in spanish is {eng_to_spa["two"]}')
eng_to_spa['three'] = 'tres'  # this is how to add information to the dictionary
eng_to_spa['two'] = 'Dos'  # this is how you change a value
print(eng_to_spa['three'])

print('Let me teach you Spanish:')
for i in eng_to_spa:
    print(f'{i} is {eng_to_spa[i]}')

