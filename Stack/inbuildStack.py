import queue
# LifoQueue() = Stack
q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(q.get())
print(q.get())
print(q.empty())