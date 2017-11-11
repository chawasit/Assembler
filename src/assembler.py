#!/usr/bin/python
import sys


def assembler_r():
    instructions = []
    in_file = open(sys.argv[2], "r")
    for line in in_file:
        instructions.append(line.split("  "))
    return instructions


if __name__ == '__main__':
    if len(sys.argv) == 3:
        assembler_r()
