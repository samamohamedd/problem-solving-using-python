from typing import Optional


class node:
    def __init__(self, value=None, n=None):
        self.value = value
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class linklist:
    def __init__(self, r=0, next=None):
        self.head = r
        self.next = next

    def append(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
        else:
            this_node = self.head
            while this_node.next_node:
                this_node = this_node.next_node
            this_node.next_node = new_node


class Solution:
    def reverseList(self, head: Optional[linklist]) -> Optional[linklist]:
        mylist = linklist()
        while head is not None:
            next = head.next
            head.next = None
            prev = head
            head = next
            mylist.append(prev)
        return mylist
