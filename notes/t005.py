MaxCount = 10**7

f = open('out.txt', 'wt')
for x in xrange(MaxCount):
    print >> f, x
f.close()