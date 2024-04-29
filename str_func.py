# str_func.py

def capitalize_words(input_string):
    """
    Принимает строку и возвращает ее с заглавными первыми буквами каждого слова.

    :param input_string: Входная строка.
    :return: Строка с заглавными первыми буквами каждого слова.
    """
    return ' '.join(word.capitalize() for word in input_string.split())

# Добавьте docstring к функции uppercase_string из предыдущего задания
def uppercase_string(input_string):
    """
    Принимает строку и возвращает ее в верхнем регистре.

    :param input_string: Входная строка.
    :return: Строка в верхнем регистре.
    """
    return input_string.upper()
