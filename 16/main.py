
words = ['rzeka', 'lato', 'zima', 'pogoda', 'deszcz']
dictionary = {'rzeka': 'river', 'lato': 'summer',
              'zima': 'winter', 'pogoda': 'weather', 'deszcz': 'rain'}
# input('Podaj słowo\n')
polish_word = input('Podaj słowo po Polsku\n')

if polish_word in dictionary:
    print(dictionary[polish_word])
else:
    print('Nie znaleziono słowa w słowniku')
