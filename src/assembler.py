#!/usr/bin/python2
import sys
import rtype
import otype
import itype
import jtype
import fill
import re
import validator

labels = {}										# create memory name label

											# regular expression each type
three_params_pattern = r"(\w*)[\t ]+(add|nand|lw|sw|beq)[\t ]+(\w*)[\t ]+(\w*)[\t ]+(-?\w*)[\t ]*(.*)"
otype_pattern = r"(\w*)[\t ]+(halt|noop)(.*)"
jtype_pattern = r"(\w*)[\t ]+(jalr)[\t ]+(\w+)[\t ]+(\w+)[\t ]*(.*)"
fill_pattern = r"(\w*)[\t ]+(.fill)[\t ]+(-?\w+)[\t ]*(.*)"

patterns = [three_params_pattern, otype_pattern, jtype_pattern, fill_pattern]

def assembler_r():								
    instructions = []
    in_file = open(sys.argv[1], "r")							# read file
    for line in in_file:								# write each line in file to instructions 
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

def write_output(machine_codes):							# write output
    file = open("machine_code.txt","w")
    for machine_code in machine_codes:
        file.write(str(machine_code) + '\n')

def check_instuction(instructions,labels):
    memory_index = 0
    result = []
    for instruction in instructions:
        opcode = instruction[1].strip()
        if(opcode == "add" or opcode == "nand"):					# check if it is r-type
            result.append(rtype.rtype(instruction))
        elif(opcode == "lw" or opcode == "sw" or opcode == "beq"):			# check if it is i-type
            result.append (itype.i_type(instruction,labels,memory_index))	
        elif(opcode == "jalr"):								# check if it is j-type
            result.append(jtype.jtype(instruction))
        elif(opcode == "halt" or opcode == "noop"):					# check if it is o-type
            result.append(otype.otype(instruction,labels))
        elif(opcode == ".fill"):							# check if it is .fill 
            result.append(fill.fill(instruction,labels))
        else:
            sys.exit("No type")
        memory_index += 1
    write_output(result)

def check_label(instructions):
    memory_index = 0
    for instruction in instructions:
        label = instruction[0].strip('\r\n')						# filter label
        if(label != ''):
            if validator.label_isvalid(labels, label):					# check if label is valid 
                labels[label] = memory_index
        memory_index += 1
    return labels

if __name__ == '__main__':
    if len(sys.argv) == 2:
        instructions = assembler_r()							# read file and store in instructions
        labels = check_label(instructions)						# check labels of each instruction
        check_instuction(instructions,labels)						# filter each instruction to their type
    sys.exit(0)
