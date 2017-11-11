#!/usr/bin/python

def halt(opcode):
    return opcode << 22 


def noop(opcode):
    return opcode << 22


def otype(instruction):
    if instruction[1] == "halt":
        opcode = 6
        return   halt(opcode)
    elif instruction[1] == "noop":
        opcode = 7
        return noop(opcode)    
