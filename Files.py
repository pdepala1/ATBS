import os, shelve

'C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'
print('\\')

print(r'C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg')

print(os.getcwd())

print(os.path.abspath('..\\pizza.jpg'))

print(os.path.isabs('..\\pizza.jpg'))
print(os.path.isabs('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))

print(os.path.relpath('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg', 'c:\\Users'))

print(os.path.dirname('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))

print(os.path.basename('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))

print(os.path.exists('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))
print(os.path.exists('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\icecream.jpg'))

print(os.path.isfile('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))
print(os.path.isfile('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files'))

print(os.path.getsize('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\pizza.jpg'))
print(os.listdir('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS'))

totalSize = 0
for filename in os.listdir('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS'):
    if os.path.isfile(os.path.join('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS', filename))

print(totalSize)

#os.makedirs('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\waffles')

helloFile = open('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\helloFile.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open('C:\\Users\\ADMINLCL\\PycharmProjects\\ATBS\\files\\helloFile2.txt.', 'w')
helloFile.write('Hello!!!!')
helloFile.write('Hello!!!!')
helloFile.write('Hello!!!!')

print(os.getcwd())

shelfFile = shelve.open('myData')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('myData')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('myData')
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(list(shelfFile.values()))