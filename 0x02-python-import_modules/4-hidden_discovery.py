#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    sort = sorted(name for name in names if not name.startswith("_"))
    for name in sort:
        print(name)
