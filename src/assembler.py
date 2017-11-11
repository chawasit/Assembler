#!/usr/bin/python
import sys

def assembler_r():
    instructions = []
    in_file = open(sys.argv[2], "r")
    for line in in_file:
        instructions.append(line.split("  "))
    return instructions

def check_instuction(instructions):
    for instruction in instructions:
        instruction = instruction[1]
        if(instruction == "add"):
            print("add")
        elif(instruction == "nand"):
            print("nand")
        elif(instruction == "lw"):
            print("lw")
        elif(instruction == "sw"):
            print("sw")
        elif(instruction == "beq"):
            print("beq")
        elif(instruction == "jalr"):
            print("jalr")
        elif(instruction == "halt"):
            print("halt")
        elif(instruction == "noop"):
            print("noop")
        else:
            print("orther")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        instructions = assembler_r()
        check_instuction(instructions)
