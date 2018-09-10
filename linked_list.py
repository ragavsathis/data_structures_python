class ragav_list(object):

    def __init__(self):
        self.top = True
        self.current_value = None
        self.current_index = None
        self.next_node = None
        self.prev_node = None

    def apppend(self,value):
        if self.top:
            a = ragav_list()
            a.current_value = value
            a.current_index = 0
            self.top = False
            self.current_index = 0
            self.current_value = a.current_value
            self.current_index = a.current_index
            self.next_node = a
        else:
            a = ragav_list()
            a.current_value = value
            self.current_value = a.current_value
            self.current_index += 1
            a.current_index = self.current_index
            a.next_node = self.next_node
            self.next_node = a

    def print_list(self):
        a = self.next_node
        while True:
            if not a:
                print "list is empty"
                break
            else:
                print a.current_value,a.current_index
                a = a.next_node

root=ragav_list()
root.apppend(10)
print root.current_value,root.current_index,root.next_node
root.apppend(20)
print root.current_value,root.current_index,root.next_node
root.apppend(30)
print root.current_value,root.current_index,root.next_node
root.apppend(40)
print root.current_value,root.current_index,root.next_node
root.apppend(50)
print root.current_value,root.current_index,root.next_node
root.print_list()

