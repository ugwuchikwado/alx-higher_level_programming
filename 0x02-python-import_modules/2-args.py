#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument: ".format(arg_count))

    else:
        print("{} arguments: ".format(arg_count))

    if len(sys.argv) > 0:
        for a in sys.argv:
            if i > 0:
                print("{:d}: {}".format(i, a))
            i += 1

