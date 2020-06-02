from glasstext import glass

text = input('plain text: ')
glasstext = glass.write(text)
reverse = glass.read(glasstext)

print('glasstext:', glasstext)
print('reversed glasstext:', reverse)

print('\n\nTry opening and reading the blank.txt file before continuing!')
input('[enter] to continue')

print('\nNow type blank.txt to load')
while True:
    c = input('filename: ')
    if c != 'blank.txt':
        print('Wrong!')
    else:
        x = glass.load(c)
        print(x)
        break

input('[enter] to close')
