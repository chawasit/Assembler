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

<<<<<<< Updated upstream
def check_instuction(instructions,labels):
=======
<<<<<<< Updated upstream
def check_instuction(instructions):
=======
def check_instuction(instructions,labels):
    memory_index = 0
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    for instruction in instructions:
        opcode = instruction[1].strip()
        if(opcode == "add" or opcode == "nand"):
            print(rtype.rtype(instruction))
        elif(opcode == "lw" or opcode == "sw" or opcode == "beq"):
<<<<<<< Updated upstream
            print (itype.i_type(instruction,labels))
=======
<<<<<<< Updated upstream
            print(rtype.rtype(instruction))
>>>>>>> Stashed changes
        elif(opcode == "jalr"):
            print("J-Type")
        elif(opcode == "halt" or opcode == "noop"):
            print(otype.otype(instruction))
<<<<<<< Updated upstream
        memory = instruction[1]
=======
        else:
            print("orther")
=======
            print (itype.i_type(instruction,labels,memory_index))
        elif(opcode == "jalr"):
            print(jtype.jtype(instruction))
        elif(opcode == "halt" or opcode == "noop" or opcode == ".fill"):
            print(otype.otype(instruction,labels))
        memory_index += 1
>>>>>>> Stashed changes
>>>>>>> Stashed changes

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
