#!/usr/bin/python2
import sys
import rtype
import otype
import itype
import jtype
import fill
import re
import validator
labels = {}

three_params_pattern = r"(\w*)[\t ]+(add|nand|lw|sw|beq)[\t ]+(\w*)[\t ]+(\w*)[\t ]+(-?\w*)[\t ]*(.*)"
otype_pattern = r"(\w*)[\t ]+(halt|noop)(.*)"
jtype_pattern = r"(\w*)[\t ]+(jalr)[\t ]+(\w+)[\t ]+(\w+)[\t ]*(.*)"
fill_pattern = r"(\w*)[\t ]+(.fill)[\t ]+(-?\w+)[\t ]*(.*)"

patterns = [three_params_pattern, otype_pattern, jtype_pattern, fill_pattern]

def assembler_r():
    instructions = []
    in_file = open(sys.argv[1], "r")
    for line in in_file:
        find = False
        instruction_group = []
        for pattern in patterns:
            m = re.match(pattern, line)
            if m is not None:
                instruction_group = m.groups()
                find = True
                break
        if not find:
            print "not match any pattern: " + str(line) 
            sys.exit(1)
        instructions.append(instruction_group)
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
        label = instruction[0].strip('\r\n')
        if(label != ''):
            if not(validator.label_isvalid(labels, label)):  
                sys.exit(1)
            else: 
                labels[label] = memory_index
        memory_index += 1
    return labels

if __name__ == '__main__':
    if len(sys.argv) == 2:
        instructions = assembler_r()
        labels = check_label(instructions)
        check_instuction(instructions,labels)
    sys.exit(0)
