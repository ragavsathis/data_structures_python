a = [1,2,3,4,5]
b = 10
c = dict()

def func1(x):
    c[x] = x+10

map(func1, (a if b==10 else list()))
print {x:x+15 for x in (a if b==10 else list()) }
print c


c = {'one':[1]}
d = c
print id(d), id(c)
c = {'2':[1,2]}
print id(d), id(c)
print d, c