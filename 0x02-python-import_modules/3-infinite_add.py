#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    idx = 0
    if (len >= 1):
        for i in range(1, len):
            idx += int(sys.argv[i])
    print("{}".format(idx))
