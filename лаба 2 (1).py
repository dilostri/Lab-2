from csv import reader

a = []
with open('books.csv', 'r', encoding='windows-1251') as file:
    a = file.readlines()

# название длиннее 30 символов
k = 0 # колво строк
for string in a:
    if len(string.split(';')[1]) > 30:
        k += 1

print(k)