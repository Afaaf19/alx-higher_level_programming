#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def args_counts():
        args = sys.argv[1:]
        argc = len(args)
        if argc > 1:
            dot = "s:"
        elif argc == 1:
            dot = ":"
        else:
            dot = "s."
        print(f"{argc} argument{dot}")
        for i in range(len(args)):
            print(f"{i+1}: {args[i]}")
args_counts()
