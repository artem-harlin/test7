large_line = ''
large_line_len = 0
filename = r'text6.txt'

with open(filename, 'r') as f:
    for line in f:
        if len(line) > large_line_len:
            large_line_len = len(line)
            large_line = line
 
print(large_line)
