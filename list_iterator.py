a = [1,2,3,4,5]
b = [[3,1,2,1],[2,2],[3,3],[4,4],[5,5]]


def log_list(c, d):
    for element in c:
        print(element)
        index = a.index(element)
        print(type(b[index]))

def find_index_in_list(d):
    for i in d:
        print i
        index_matched = i.index(1)
        print index_matched


if __name__ == "__main__":
    #log_list(iter(a), iter(b))
    find_index_in_list(b)