#!/usr/bin/python2
import sys
import rtype
import otype
import itype
import jtype
import fill
import re
labels = {}

def assembler_r():
    instructions = []
    in_file = open(sys.argv[2], "r")
    for line in in_file:
        instructions.append(re.split("\t| ",line))
    return instructions

def write_output(machine_codes):
    file = open("machine_code.txt","w")
    for machine_code in machine_codes:
        file.write(str(machine_code) + '\n')

def check_instuction(instructions,labels):
    memory_index = 0
    result = []
    for instruction in instructions:
        opcode = instruction[1].strip()
        if(opcode == "add" or opcode == "nand"):
            result.append(rtype.rtype(instruction))
        elif(opcode == "lw" or opcode == "sw" or opcode == "beq"):
            result.append (itype.i_type(instruction,labels,memory_index))
        elif(opcode == "jalr"):
            result.append(jtype.jtype(instruction))
        elif(opcode == "halt" or opcode == "noop"):
            result.append(otype.otype(instruction,labels))
        elif(opcode == ".fill"):
            result.append(fill.fill(instruction,labels))
        else:
            print instruction[2]
        memory_index += 1

    write_output(result)

def check_label(instructions):
    memory_index = 0
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
        for i in instructions:
            print i
        # labels = check_label(instructions)
        # check_instuction(instructions,labels)
