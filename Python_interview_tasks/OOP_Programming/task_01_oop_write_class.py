"""
Объектно-ориентированное программирование.

Задача: Написать стек (класс), который поддерживает push, pop, top и get_min (получение минимального элемента)
        за постоянное время. То есть это некоторый класс Stack и надо его реализовать.

        push - добавляет в стек
        pop - достает последний добавленный элемент из стека с удалением элемента из стека
        top - получает последний добавленный элемент из стека без удаления этого элемента
        get_min - получение минимального элемента в стеке

Задание кандидату #1: Написать код для этой задачи (текст задачи приведен выше). Для простоты принимаем, что
                      в стеке могут хранить целые числа.

Ответ на задание #1. Смотри код ниже (если код закомментирован, то можно его раскомментировать для запуска).
Эта реализация использует штатный метод MIN, имеющийся в Python.
"""

# class Stack:
#
#     def __init__(self):
#         self.my_stack = []
#
#     def push(self, element):
#         self.my_stack.append(element)
#
#     def pop(self):
#         return self.my_stack.pop()
#
#     def top(self):
#         return self.my_stack[-1]
#
#     def get_min(self):
#         return min(self.my_stack)
#
# if __name__ == "__main__":
#     my_stack = Stack()
#     my_stack.push(14)
#     my_stack.push(4)
#     my_stack.push(5)
#     my_stack.push(12)
#
#     print(f"Min: {my_stack.get_min()}")
#     print(f"Последний элемент (без его удаления): {my_stack.top()}")
#     print(f"Последний элемент (ПЕРЕД его удалением): {my_stack.pop()}")
#     print(f"Последний элемент (ПОСЛЕ его удаления): {my_stack.top()}")
#     print(f"Min (после удаления элемента): {my_stack.get_min()}")


"""
Задание кандидату #2: Далее можно попросить кандидата изменить этот код так, чтобы НЕ ИСПОЛЬЗОВАТЬ метод MIN,
имеющийся в Python штатно.

Ответ на задание #2. Смотри код ниже (если код закомментирован, то можно его раскомментировать для запуска).
Эта реализация уже БЕЗ ИСПОЛЬЗОВАНИЯ штатного метод MIN, имеющегося в Python.

Либо вообще не просить кандидата писать этот код, а дать ему уже готовый код и пусть он расскажет поподробнее о том,
что делает этот код и главное как он это делает.
"""
class Stack:

    def __init__(self):
        self.my_stack = []
        self.sorted_num = []

    def __str__(self):
        return str(self.my_stack)

    def push(self, element):
        self.my_stack.append(element)
        if len(self.sorted_num) == 0 or element <= self.sorted_num[-1]:
            self.sorted_num.append(element)

    def pop(self):
        latest_element = self.my_stack.pop()
        if latest_element == self.sorted_num[-1]:
            self.sorted_num.pop()
        return latest_element

    def top(self):
        return self.my_stack[-1]

    def get_min(self):
        return self.sorted_num[-1]

if __name__ == "__main__":

    print("Нужный класс написан без использования метода Min(). А этот код ниже для проверки работоспособности.")
    my_stack = Stack()
    my_stack.push(14)
    my_stack.push(2)
    my_stack.push(1)
    my_stack.push(7)
    my_stack.push(5)
    my_stack.push(12)
    my_stack.push(3)
    my_stack.push(7)

    print(f"Min: {my_stack.get_min()}")
    print(f"Последний элемент (без его удаления): {my_stack.top()}")
    print(f"Последний элемент (ПЕРЕД его удалением): {my_stack.pop()}")
    print(f"Последний элемент (ПОСЛЕ его удаления): {my_stack.top()}")
    print(f"Min (после удаления элемента): {my_stack.get_min()}")

    my_stack.pop()
    print(f"Min (после удаления элемента): {my_stack.get_min()}")
    my_stack.pop()
    print(f"Min (после удаления элемента): {my_stack.get_min()}")
    my_stack.pop()
    print(f"Min (после удаления элемента): {my_stack.get_min()}")
    my_stack.pop()
    print(f"Min (после удаления элемента): {my_stack.get_min()}")
    my_stack.pop()
    print(f"Min (после удаления элемента): {my_stack.get_min()}")

    print(my_stack)
