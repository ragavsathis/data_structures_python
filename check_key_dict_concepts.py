a = {'ragav':[1,2,3, 4, 5]}


def check_min(x):
    return x>0


print map(lambda x: check_min(x), a.get('raav',list()))
if map(lambda x: check_min(x), a.get('raav',list())):
    print "all validation passes"
else:
    print "failed"
