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

'''Завдання 1
Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
елементами:
■ IsEmpty — перевірка, чи черга пуста;
■ IsFull — перевірка черги на заповнення;
■ Enqueue — додати новий елемент до черги;
■ Dequeue — видалення елемента з черги;
■ Show — відображення на екрані всіх елементів черги.
На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.'''

import time


class SymbolQueue:
    def __init__(self, size=0):
        self.size = size
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def show(self):
        return self.items

    def show_like_human(self):
        for item in self.items:
            time.sleep(0.4)
            print(item, end='')
        print()

    def enqueue(self, item):
        if (len(self.items) <= self.size) or (self.size == 0):
            if (type(item) == str) and (len(item) == 1):
                self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.size > 0:
            if self.size == len(self.items):
                return True
            else:
                return False


room = SymbolQueue()
room.enqueue('1')
room.enqueue('2')
room.enqueue('3')
room.enqueue('4')
room.enqueue('5')
room.enqueue('6')
room.enqueue('7')
print(room.is_full())