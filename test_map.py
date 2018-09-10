a = (1, 2, 3)
b = [4, 5, 6, 7]
c = a
print id(a)
a = map(lambda x,y: (x,y), a, b)
print a, id(a), id(c)
print zip(b,c)


def filter_func(x,y):
    if (x + y) > 10:
        return 1
    else:
        return 0


print map(filter_func, b, b)

f = [1, 4, 3, 5, 10, -1]
f1 = [2, 4, 6, 8, 11, -5]
func1 = lambda x, y: (x == y)
result = map(func1, f, f1)
print result
if bool(False) in result:
    print "List is not same"
else:
    print "List is same"
