__author__ = 'daniela.zagorska'
fname = raw_input('Enter the file name: ')
try:
    fhand = open(r"C:\Users\daniela.zagorska\Documents\PycharmProjects\Dani-Python\problems\\" + fname)
except:
   exit()
counts = dict()
for line in fhand:
     if len(line)>0:
        words = line.split(' ')
        if words[0]== 'From':
            if words[1] in counts:
                counts[words[1]] += 1
            else:
                counts[words[1]] = 1
keys = counts.keys()
maxkey = keys[0]
for key,value in counts.iteritems():
    if value > counts[maxkey]:
        maxkey=key

print maxkey,counts[maxkey]

