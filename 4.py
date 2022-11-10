bukv = 0 
slov = 0
strok = 0 
for line in open('text4.txt', 'r'):     
      strok += 1      
      bukv += len(line)      
      pos = 'out'
      
      for letter in line:   
          
          if letter != ' ' and pos == 'out':            
              slov += 1     
              pos = 'in'       
          elif letter == ' ':            
              pos = 'out'

print("bukv:", bukv)
print("slov:", slov)
print("strok:", strok)
