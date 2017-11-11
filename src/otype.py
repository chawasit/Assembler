#!/usr/bin/python

def otype(instruction,labels):
    if instruction[1].strip('\n') == "halt":
        opcode = 6
        return opcode << 22 
    elif instruction[1].strip('\n') == "noop":
        opcode = 7
        return opcode << 22    
    elif instruction[1].strip('\n') == ".fill":
        try:
            return int(instruction[2].strip('\n'))
        except:
            return labels[instruction[2].strip('\n')]