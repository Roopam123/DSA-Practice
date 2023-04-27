class QueueUsingTwoStack:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self,data):
        while (len(self.__s1)!=0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while (len(self.__s2)!=0):
            self.__s1.append(self.__s2.pop())
    def dequeue(self):
        if len(self.__s1)==0:
            return -1
        return self.__s1.pop()
    def front(self):
        if len(self.__s1)==0:
            return -1
        return self.__s1[-1]
    def size(self):
        return len(self.__s1)
    def isEmpty(self):
        return self.size()==0 
    
q = QueueUsingTwoStack()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
print(q.dequeue())
print(q.size())
print(q.front())
print(q.isEmpty())