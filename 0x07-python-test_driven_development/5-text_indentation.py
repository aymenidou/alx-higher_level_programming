#!/usr/bin/python3
"""text_indentation module
"""


def text_indentation(text):
    """print text with indentation"""
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    word = True
    for i in range(len(text)):
        if (text[i] in ".?:"):
            print("{}\n".format(text[i]))
            word = False
        else:
            if (text[i] != " "):
                word = True
            if (word):
                print(text[i], end="")
