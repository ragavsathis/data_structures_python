a = [1,2,3]
b = []
index = a.index(1)
print index
try:
    b[index].append([1,2])
except Exception as e: 
    print "list is not present"
    b.insert(index,list())
    b[index].append([1,2])
print b, dir(b)


class A():
    @staticmethod
    def a_b():
        print("python 3 is used")

a =A()
c=['a','b']
print(dir(a))
a.a_b()
# d = "{}_{}".format(c[0],c[1])
# print(d)
getattr(a,d)()

a = [1,2,3]
c = [4,5,6]
e = map(lambda x,y,z:x+y-z, a, c, a)
print e, type(e)
b = a * 3
print b
d = a + c
print d
