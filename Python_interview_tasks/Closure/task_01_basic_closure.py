"""
Замыкания.

Довольно непростая для понимания тема. Не сложная, но непростая для понимания. Лучше разбираться на примерах.
Несмотря на все сложности необходимо понимать что это такое, ибо оно реально используется. Например, в декораторах.

Вопросы кандидатам:

- Вопрос #1: Что такое замыкания в Python и для чего они нужны?

Ответ на вопрос #1: <...>


- Вопрос #2: Как работает этот код?

Ответ на вопрос #2: Обе функции f() и h() возвращают замыкание.
                    Но в идеале кандидат должен рассказать про это подробнее.
"""

def f(x):
    def g(y):
        return x + y
    return g   # Возвращает замыкание.

def h(x):
    return lambda y: x + y  # Возвращает замыкание.

a = f(2)
print(a(3))

b = h(7)
print(b(3))


"""
- Вопрос #3: Как работает этот код? Что будет выведено на экране в результате его выполнения?  

Ответ на вопрос #3: Выведется 7, а не 6.
"""
x = 2

def f(y):
    return x + y

def g(z):
    x = 1
    return f(z)

print(g(5))


"""
- Вопрос #4: Как изменить функцию g(z) в представленном выше коде таким образом, чтобы в результате работы этой
 программы на экран была выведено число 6 ?

Условия выполнения:
- Изменять можно ТОЛЬКО функцию g(z), другие функции не трогать!  
- Функция g(z) должна возвращать строго f(z), то есть строку return f(z) изменять запрещено!   

Ответ на вопрос #4: Обновленная функция g(z) будет выглядеть теперь вот так:
"""

def g(z):
    global x
    x = 1
    return f(z)

"""
и тогда приведенный выше код вернет число 6, а не 7.
"""
