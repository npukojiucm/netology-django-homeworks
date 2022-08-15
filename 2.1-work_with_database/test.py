import csv

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))

print(phones[0]['name'].replace(' ', '-').lower())

