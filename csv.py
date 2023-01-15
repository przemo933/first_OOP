with open('rozliczenie.csv', 'r') as plik_csv:
    content = plik_csv.readlines()
#print(content)
#print(content[4])
x = 'mama.tata.pies.kot'
y = x.split('.')

for i in range (len(content)):
    content[i] = content[i].split(',')
print(content[0])
print(content[4])
print(content[4][2])

#oblicz srednia wyplate
suma = 0
liczba_rekordow = len(content)-1

for i in range(1, len(content)):
    suma += int(content[i][1])

print(suma / liczba_rekordow)

#oblicz osoby na macierzynskiem
licznik = 0

for i in range(1, len(content)):
    content[i][4] = content[i][4].replace('\n','')
    if content[i][4] == 't' and content[i][3] == 'k':
        licznik += 1

print(licznik)

