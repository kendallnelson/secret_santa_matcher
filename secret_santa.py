import random

santa_givers= ['NAME']

name_addr = {'NAME':'ADDRESS'}


keys = list(name_addr.keys())
random.shuffle(keys)

index = 0

for santa in santa_givers:
 file = santa + '.txt'
 f = open(file, 'w')
 name = keys[index]
 Address = name_addr[name]
 f.write ('Hello %s, ' % santa)
 f.write("\n\nYou are going to be buying for: %s" % name)
 f.write("\n\nShipping Address: %s" % Address)
 f.write ("\n\nMerry Christmas!")
 f.close()
 index= index +1
 
##MAKE SURE NO ONE IS GIVING TO THEMSELVES##
