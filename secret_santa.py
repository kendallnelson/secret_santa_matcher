import random

santa_givers= ['NAME',]

name_addr = {'NAME':'ADDRESS',
            }

keys = list(name_addr.keys())
random.shuffle(keys)


print "Givers: "
print santa_givers
print
print "Control Recievers: "
print name_addr
print 
print "Random Recievers"
print [(key, name_addr[key]) for key in keys]

index = 0

for santa in santa_givers:
    print santa
