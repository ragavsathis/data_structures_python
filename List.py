
# Understanding Lists
a = [1, 3, 4, 7, 8]
x = [11, 12, 13, 14, 15, 15, 15]
a.append(1)
print len(a)
print a
b = a.pop(2)
print b
c = a.pop()
print c
print a
a[1:] = [10]
print a
a[1:] = x
print a
print a.count(15)
