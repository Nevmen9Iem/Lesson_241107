# Черга (Queue)

# Черга (queue) — це структура даних, яка використовується для роботи з даними,
# що відображаються вперед-назад.

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# l.append(10)
#
# l.append(11)
#
# print(l.pop(0))
# print(l.pop(0))

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def __repr__(self):
#         return str(self.items)
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
# room = Queue()
# room.enqueue(123)
# room.enqueue(456)
# print(room)
# print(room.dequeue())
# print(room.dequeue())

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def __repr__(self):
#         return repr(self.items)
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
# room = Queue()
# room.enqueue(123)
# room.enqueue(456)
# print(room)
# print(room.dequeue())
# print(room.dequeue())
# print(room)