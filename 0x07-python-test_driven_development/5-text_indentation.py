#!/usr/bin/python3
"""text_indentation module
"""


def text_indentation(text):
    """print text with indentation"""
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i] in ".?:"):
            print("{}\n".format(text[i]))
        else:
            if (i > 0 and text[i - 1] in ".?:" and text[i] == " "):
                continue
            print(text[i], end="")
