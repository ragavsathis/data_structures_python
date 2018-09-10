################## Understanding list assignment ##################
a = [1, 3, 4, 5, 6]
b = a
print id(a), id(b)
a.append(5)
print b
if a == b: print "list is same"

################### Understanding Zip usage #################################
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
d = [1, 3, 5]
c = zip(a, b)
e = set(c)

print c, type(c), e
if c == e:
    print "both zip are same"
else:
    print "Both Zip items are different"

####################################################################
a = [1, 2, 4, 3]
b = [5, 6, 7, 8]
c = [1, 2, 3, 4]
d = zip(a, b, c)
print d[0], len(d[0]), type(d[0])
e = dict(d)
print e

