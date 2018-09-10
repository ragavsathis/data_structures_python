# from collections import OrderedDict

# a = OrderedDict([
#     ('one', [1,2]),
#     ('two', [3,4]),
# ])

# print a.values(), zip(*a.values())


# a= [1,2,3]
# if len(a) % 2:
#     print "len of a is odd"


def ragav(x):
    if x % 2:
        raise Exception ("number is even")
    else:
        yield x

a = ragav(11)
map(lambda x: x, a)