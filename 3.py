with open('text3.txt') as t:
      print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
