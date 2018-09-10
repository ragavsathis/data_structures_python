a = [1, 2, 3]
b = [10, 20, 30]
x = zip(a,b)
c = dict(zip(a,b))
d = dict(enumerate(a))
print d,c

e = list(enumerate(b))
f = tuple(enumerate(b))
print e,f

for i,j in x:
    print i, j