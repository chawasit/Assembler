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
        if(instruction == "add" or instruction == "nand"):
            print("I-Type")
        elif(instruction == "lw" or instruction == "sw" or instruction == "beq"):
            print("R-Type")
        elif(instruction == "jalr"):
            print("J-Type")
        elif(instruction == "halt" or instruction == "noop"):
            print("O-Type")
        else:
            print("orther")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        instructions = assembler_r()
        check_instuction(instructions)
