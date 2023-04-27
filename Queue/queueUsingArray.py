class Queue:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0
    
    def enqueue(self,data):
        self.__arr.append(data)
        self.__count = self.__count+1

    def dequeue(self):
        if self.isEmpty() is True:
            print("Hey! Queue is Empty")
            return
        element = self.__arr[self.__front]
        self.__front = self.__front+1
        self.__count = self.__count-1
        return element
    def front(self):
        return self.__arr[self.__front]
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size() == True
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.front())
print(q.size())
print(q.isEmpty())
