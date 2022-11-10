import mmap

with open('text2.txt', 'rb', 0) as file, \
      mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
      if s.find(b's') != -1:
          print('True')
      else:
          print('False')
