class Node:
    def __init__(self,data):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self,element):
        newNode=Node(element)
        if self.__head is None:
            self.__head=newNode
            
        else:
            self.__tail.next=newNode
            
        self.__tail=newNode
        self.__count=self.__count+1
    def dequeue(self):
        if self.__head is None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data
    def front(self):
        if self.__head is None:
            return -1
        return self.__head.data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size() == 0
    

q = Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.front())
print(q.size())
print(q.isEmpty())