#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argv == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 arguments:")
    else:
        print(f"{argc} arguments:")

    for i, arg in enumerate(argv[1:], 1):
        print(f"{i}: {arg}")
