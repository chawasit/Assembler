#!/usr/bin/python2
import sys
import rtype
import otype
import itype
import jtype
import fill
import re
import validator

# create memory name label
labels = {}			

# regular expression each type
three_params_pattern = r"(\w*)[\t ]+(add|nand|lw|sw|beq)[\t ]+(\w*)[\t ]+(\w*)[\t ]+(-?\w*)[\t ]*(.*)"
otype_pattern = r"(\w*)[\t ]+(halt|noop)(.*)"
jtype_pattern = r"(\w*)[\t ]+(jalr)[\t ]+(\w+)[\t ]+(\w+)[\t ]*(.*)"
fill_pattern = r"(\w*)[\t ]+(.fill)[\t ]+(-?\w+)[\t ]*(.*)"

patterns = [three_params_pattern, otype_pattern, jtype_pattern, fill_pattern]

def assembler_r():								
    instructions = []

    # read file
    in_file = open(sys.argv[1], "r")	

    # write each line in file to instructions 	
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

# write output
def write_output(machine_codes):							
    file = open("machine_code.txt","w")
    address_count = 0

    for machine_code in machine_codes:
        hex_code = hex(machine_code)  if machine_code >= 0 else  hex(machine_code & 0xffff)
        print("(address " + str(address_count) 
                          + "): " 
                          + str(machine_code) 
                          + " (hex " 
                          + str(hex_code) 
                          + ")")
        address_count += 1
        file.write(str(machine_code) + '\n')

def check_instuction(instructions,labels):
    memory_index = 0
    result = []
    for instruction in instructions:
        opcode = instruction[1].strip()

        # check if it is r-type
        if(opcode == "add" or opcode == "nand"):					
            result.append(rtype.rtype(instruction))

        # check if it is i-type
        elif(opcode == "lw" or opcode == "sw" or opcode == "beq"):			
            result.append (itype.i_type(instruction,labels,memory_index))	

        # check if it is j-type
        elif(opcode == "jalr"):								
            result.append(jtype.jtype(instruction))
        
        # check if it is o-type
        elif(opcode == "halt" or opcode == "noop"):					
            result.append(otype.otype(instruction,labels))
        
        # check if it is .fill 
        elif(opcode == ".fill"):							
            result.append(fill.fill(instruction,labels))
        
        else:
            sys.exit("No type")
        memory_index += 1
    write_output(result)

def check_label(instructions):
    memory_index = 0
    for instruction in instructions:
        
        # filter label
        label = instruction[0].strip('\r\n')						
        if(label != ''):
            
            # check if label is valid 
            if validator.label_isvalid(labels, label):					
                labels[label] = memory_index

        memory_index += 1
    return labels

if __name__ == '__main__':
    if len(sys.argv) == 2:
        
        # read file and store in instructions
        instructions = assembler_r()							
        
        # check labels of each instruction
        labels = check_label(instructions)						
        
        # filter each instruction to their type
        check_instuction(instructions,labels)						
    sys.exit(0)
