__author__ = 'daniela.zagorska'

fname = raw_input('Enter the file name: ')
    #try:

import os
print os.path.isfile(r"C:\Users\daniela.zagorska\Documents\PycharmProjects\Dani-Python\problems\romeo.txt")
fhand = open(r"C:\Users\daniela.zagorska\Documents\PycharmProjects\Dani-Python\problems\\" + fname)
#except:
 #  exit()
counts = dict()
for line in fhand:
    words = line.split()
for word in words:
    if word not in counts:
        counts[word] = 1
else:
    counts[word] += 1
print counts