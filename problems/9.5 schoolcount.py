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
            domain = words[1].split('@')[1]
            if domain in counts:
                counts[domain] += 1
            else:
                counts[domain] = 1
print counts