# class Queue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self, x):
#         self.stack1.append(x)
#
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 p = self.stack1.pop()
#                 self.stack2.append(p)
#         return self.stack2.pop()
#
# # q = Queue()
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(5)

# print(q.stack1)
#
# q.dequeue()
'''
while self.stack1:: This checks if there are still elements in self.stack1. In Python, an empty list is considered as False in a boolean context, and a non-empty list is considered as True. So, while self.stack1: will continue as long as there are elements in self.stack1.

self.stack2.append(self.stack1.pop()): This line is doing two things:

self.stack1.pop(): This pops (removes and returns) the last element from self.stack1. The pop() method in Python removes the last element from the list and returns it.

self.stack2.append( ... ): This appends (adds) the element we just popped from self.stack1 to self.stack2.

In summary, this code is transferring all elements from self.stack1 to self.stack2, one by one, in reverse order. This is because a stack is a Last-In-First-Out (LIFO) data structure, so popping elements from self.stack1 and immediately appending them to self.stack2 results in the elements being in reverse order in self.stack2. This is a key part of how a queue (a First-In-First-Out, or FIFO, data structure) is implemented using two stacks.
'''


class Que:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    def inq(self,x: int):
        self.stack_1.append(x)

    def dnq(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

q =Que()
q.inq(3)
q.inq(4)
q.inq(6)

print(q.stack_1)

s = q.dnq()
print(s)