class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count+1

    def pop(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count-1
        return data
    def top(self):
        if self.isEmpty() is True:
            print("Hey! Stack is Empty")
            return
        return self.__head.data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0
    

s = Stack()
s.push(10)
s.push(11)
s.push(12)
s.push(13)

print(s.pop())
print(s.size())
print(s.top())
print(s.isEmpty())