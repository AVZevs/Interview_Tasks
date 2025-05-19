"""
Декораторы для джуниор.
Это довольно частый вопрос на собесах. Плюс декораторы реально часто используются.

Чтобы понять, что за код здесь написан - прочитай комментарии в файле task_01_decorators_junior.py

Если коротко, там было дано задание переписать тот код, который написан в файле task_01_decorators_junior.py
вот таким образом (это был как раз Вопрос #4):

- Вопрос #4: Как видно в функциях ZZZ_text_outer(func) используется практически одинаковый код. Имеет смысл
вынести этот код в отдельную функцию и ОЧЕНЬ ЖЕЛАТЕЛЬНО решить этот вопрос также с использованием декораторов.
Попросить кандидата сделать это.

Ответ на вопрос #4:

Вот здесь я как раз и реализовал этот код. С использованием декораторов с параметрами. Здесь уже нет смысла
использовать несколько декораторов, достаточно одного.
"""
from base64 import b64decode

def outer_text(left: str, right: str):
    def three_text_outer(func):
        def wrapper(*args, **kwargs):
            #left, right = "0JrQsNC20LTRi9C5", "0YTQsNC30LDQvS4="
            result = (f"{b64decode(left.encode("utf-8")).decode("utf-8")} {func(*args, **kwargs)} "
                      f"{b64decode(right.encode("utf-8")).decode("utf-8")}")
            return result
        return wrapper
    return three_text_outer


@outer_text("0JrQsNC20LTRi9C5", "0YTQsNC30LDQvS4=")
@outer_text("0L7RhdC+0YLQvdC40Lo=", "0YHQuNC00LjRgg==")
@outer_text("0LbQtdC70LDQtdGC", "0LPQtNC1LA==")
def print_basic_text(basic_text: str) -> str:
    return f"{b64decode(basic_text.encode("utf-8")).decode("utf-8")}"

if __name__ == "__main__":
    print(print_basic_text("0LfQvdCw0YLRjA=="))
