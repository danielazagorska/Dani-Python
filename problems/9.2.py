__author__ = 'daniela.zagorska'
fname = raw_input('Enter the file name: ')
try:
    #import os
    #print os.path.isfile(r"C:\Users\daniela.zagorska\Documents\PycharmProjects\Dani-Python\problems\\")
    fhand = open(r"C:\Users\daniela.zagorska\Documents\PycharmProjects\Dani-Python\problems\\" + fname)
except:
   exit()
counts = dict()
for line in fhand:
    if len(line)>0:
        words = line.split(' ')
        if words[0]== 'From':
            if words[2] in counts:
                counts[words[2]] = counts[words[2]]+1
            else:
                counts[words[2]] = 1
print(counts)

