"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        previous = self.tail
        self.tail = new_node
        self.tail.set_prev(previous)
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_prev()
            self.length -= 1
            return value

    def contains(self, value):
        if self.head is None:
            return None
        found = False
        cur_node = self.head
        cur_val = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() == value:
                found = True
            cur_node = cur_node.get_next()

        return found

    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()

        return cur_max


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if (self.storage.length > 0):
            return self.storage.length
        else:
            return 0

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if (self.storage.length > 0):
            return self.storage.remove_head()
