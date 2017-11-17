#!/usr/bin/python

def otype(instruction,labels):
    if instruction[1].strip('\r\n') == "halt":
        opcode = 6
        return opcode << 22 
    elif instruction[1].strip('\r\n') == "noop":
        opcode = 7
        return opcode << 22    
