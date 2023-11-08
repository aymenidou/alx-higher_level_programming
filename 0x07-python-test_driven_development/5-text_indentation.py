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
            i += 1;
        else:
            if (i > 0 and text[i - 1] in ".?:"):
                continue
            print(text[i], end="")
