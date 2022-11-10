file = open('text7.txt', 'r')
s = file.readlines()
s.reverse()
print(''.join(s))
