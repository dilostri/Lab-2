from csv import reader

a = []
with open('books.csv', 'r', encoding='windows-1251') as file:
    a = file.readlines()


from random import randrange
num_str = [randrange(0, 9410) for i in range(20)]

with open('result.txt', 'w', encoding='utf-8') as ssylki:
    for i in num_str:
        # var = a[i].split(';')[3] + '. ' + a[i].split(';')[1] + ' - год написания. которого нет в таблице'
        ssylki.write(a[i].split(';')[3] + '. ' + a[i].split(';')[1] + ' - год написания, которого нет в таблице + \n' )
print(var)