import random

eng_to_spa = {'hello': 'hola', 'yes': 'sí', 'dictionary': 'diccionario',
              'one': 'uno', 'two': 'dos', 'no': 'no'}
if 'hello' in eng_to_spa:
    print('I know how to sayhello in Spanish')
else:
    print('I do not know how to say hello in Spanish')

print(list(eng_to_spa.values()))
print(list(eng_to_spa.keys()))

print(f'Random word of the day: ', random.choice(list(eng_to_spa.values())))

random_word = random.choice(list(eng_to_spa.keys()))
answer = input(f'How do you say {random_word} in Spanish?')
if answer == eng_to_spa[random_word]:
    print('Well done')
else:
    print(f'The correct answer was {eng_to_spa[random_word]}')
