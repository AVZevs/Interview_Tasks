"""
ЗЫ. Как по мне, то это довольно сложная задачка. Это уже скорее уровень senior.

Это довольно частый вопрос на собесах. Плюс декораторы реально часто используются.

- Вопрос #1: Что такое декораторы в Python и для чего они нужны?

Ответ на вопрос #1:

Тут много печатать надо. Надо, чтобы собеседующий сам понимал суть этого понятия.


- Вопрос #2: Напишите декоратор, который принимает в качестве аргумента список таплов (tuple) исключений и callback'ов,
который при исключении вызывает соответствующий callback.

Вам дан вот такой код (приведен ниже), в котором уже описаны функции foo(), bar() и создано начало для описания
собственно нужного нам декоратора.


- Вопрос #3: Вместо написания кода с нуля, можно показать пользователю уже этот готовый код и попросить его
рассказать, как работает этот код, что тоже не очень-то просто на самом деле, если кандидат без опыта.
"""

from random import randint
from collections.abc import Callable
from functools import wraps

def decorator(exceptions: list[tuple[Exception, Callable[[], None]]]):
    def decorator_in(func):
        @wraps(func)
        def wrapper_one(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                for ex in exceptions:
                    if isinstance(e, ex[0]):
                        ex[1]()
                        raise e
            return result
        return wrapper_one
    return decorator_in


def bar():
    print(1)

@decorator([(KeyError, bar), (IndexError, lambda : print(2))])
def foo():
    if randint(1, 2) == 1:
        raise KeyError("bar")
    else:
        raise IndexError

if __name__ == "__main__":
    foo()
    #print(my_raise)
