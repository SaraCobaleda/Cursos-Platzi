from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data

        else:
            return "el stack esta vacio"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "el stack esta vacio"

    def clear(self):
        while self.top:
            self.pop()

    def IsInTheList(self, data):
        busca = data
        while self.top and busca != self.top.data:
            self.top = self.top.next
            if self.top.data == busca:
                print(busca)

    def recorrer(self):
        while self.top:
            print(self.top.data)
            self.top = self.top.next

