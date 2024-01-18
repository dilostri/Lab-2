from csv import reader

a = []
with open('books.csv', 'r', encoding='windows-1251') as file:
    a = file.readlines()

#поиск книги по автору без ограниичений
search = input('Search for: ')
for i in a:
    if search in i.split(';')[3] or search in i.split(';')[4]:
        print(i.split(';')[4] ,i.split(';')[1])