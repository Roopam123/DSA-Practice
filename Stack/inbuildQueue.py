# This is a Inbuild lybarray
import queue

s = queue.Queue()
s.put(10)
s.put(11)
s.put(12)
s.put(13)
print(s.get())
print(s.get())
print(s.empty())