# a = [1, 2, 3]
# b = list()
#
# # for index, value in enumerate(a, 20):
# #     b.append((index, value))
# # print b
# c = enumerate(a)
# a = 0
# try:
#     while c:
#         (a,b) = c.next()
#         print a,b
#         #b.append()
#         a += 1
#         #print c.next()
#         #b.append(c.next)
# except Exception as e:
#     print "Enumerate done with exception" + str(e)
#     print b, a

# a= [(1,"aragv"),(2,"praveen")]
# b = ["ragav", "praveen"]
# print zip(b,range(len(b)))
# d =enumerate(a)
# print d


class ragav(object):
    pass

class selvam(ragav):
    pass

a = ragav()
b = selvam()
print a.__class__, b.__class__