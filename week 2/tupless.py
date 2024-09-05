#sets

cats = set() #create empty set 
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)


birds = {'owl', 'robin','swan'}
print(birds)
birds.add('robin')
print(birds)
birds.remove('owl')
birds.add('cardinal')
print(birds)

for bird in birds:
    print(bird)


bird_list = ['robin', 'cardinal', 'swan','robin', 'cardinal', 'swan']
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)