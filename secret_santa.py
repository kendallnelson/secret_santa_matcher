import random
import csv

santa_givers= []
name_addr = {}

with open('santas.csv') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter= ',')
   for row in csv_reader:
      santa_givers. append(row[0])
      name_addr.update({row[0]:row[1]})

print  santa_givers

keys = list(name_addr.keys())
random.shuffle(keys)

index = 0

for santa in santa_givers:
   if santa is keys[index]:
      keys = list(name_addr.keys())
      random.shuffle(keys)
   else:
      file = santa + '.txt'
      f = open(file, 'w')
      name = keys[index]
      address = name_addr[name]
      f.write ('Hello %s, ' % santa)
      f.write("\n\nYou are going to be buying for: %s" % name)
      f.write("\n\nShipping Address: %s" % address)
      f.write ("\n\nMerry Christmas!")
      f.close()
      index= index +1
      santa_givers.remove(santa)
      
