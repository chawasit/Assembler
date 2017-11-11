#!/usr/bin/python2
import sys
import rtype
import otype
import itype

def assembler_r():
    instructions = []
    in_file = open(sys.argv[2], "r")
    for line in in_file:
        instructions.append(line.split("\t"))
    return instructions

def check_instuction(instructions,labels):
    for instruction in instructions:
        opcode = instruction[1].strip()
        if(opcode == "add" or opcode == "nand"):
            print(rtype.rtype(instruction))
        elif(opcode == "lw" or opcode == "sw" or opcode == "beq"):
            print (itype.i_type(instruction,labels))
        elif(opcode == "jalr"):
            print("J-Type")
        elif(opcode == "halt" or opcode == "noop"):
            print(otype.otype(instruction))
        memory = instruction[1]

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
    return labels

if __name__ == '__main__':
    if len(sys.argv) == 3:
        instructions = assembler_r()
        labels = check_label(instructions)
        check_instuction(instructions,labels)
