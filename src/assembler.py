#!/usr/bin/python2
import sys

def assembler_r():
    instructions = []
    in_file = open(sys.argv[2], "r")
    for line in in_file:
        instructions.append(line.split("  "))
    return instructions

def check_instuction(instructions):
    for instruction in instructions:
        instruction = instruction[1].strip()
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

def check_label(instructions):
    memory_index = 0
    labels = {}
    for instruction in instructions:
        label = instruction[0].strip()
        if(label != ''):
            if labels.has_key(label): 
                print("error")
            else: 
                labels[label] = memory_index
        memory_index += 1
    print(labels)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        instructions = assembler_r()
        check_label(instructions)
        check_instuction(instructions)
