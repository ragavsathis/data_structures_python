#!/usr/bin/python3

class Node(object):
    def __init__(self, data=0):
        self.data = data
        self.next_node = None

    def get_value():
        return self.data

    def set_next_node(node_obj):
        self.next_node = node_obj


class RagavLinkedList(object):

    def __init__(self):
        self.top_node = None
        self.len = 0

    @staticmethod
    def _get_new_node(data_val):
        return Node(data_val)

    def _get_last_node(self):
        tmp_node = self.top_node
        while tmp_node.next_node != None:
            tmp_node = tmp_node.next_node
        return tmp_node
    
    def __len__(self):
        return self.len

    def append(self,value):
        NewNode = Node(value)
        if not self.top_node:
            self.top_node = NewNode
        else:
            last_node = self._get_last_node()
            last_node.next_node = NewNode
        self.len += 1

    def print_list(self):
        tmp_node = self.top_node
        if tmp_node:
            index = 0
            while tmp_node.next_node != None:
                print("Index - {}\tNode value - {}".format(index, tmp_node. data))
                index += 1
                tmp_node = tmp_node.next_node
            print("Index - {}\tNode value - {}".format(index, tmp_node. data))
        else:
            print("List is empty")


if __name__ == "__main__":
    test_list = RagavLinkedList()
    test_list.print_list()
    test_list.append(10)
    test_list.append(20)
    test_list.append(30)
    test_list.append(40)
    test_list.append(50)
    test_list.append(60)
    test_list.append(70)
    test_list.append(80)
    test_list.print_list()
    print(len(test_list))