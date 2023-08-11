#!/usr/bin/python3
if __name__ == "__main__":
    """addition of one or more numbers"""
    import sys

    def args_counts():
        args = sys.argv[1:]
        argc = len(args)
        res = 0

        for i in range(argc):
            res += int(args[i])
        print(res)
args_counts()

