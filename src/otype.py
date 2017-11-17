#!/usr/bin/python

def otype(instruction,labels):
    if instruction[1].strip('\r\n') == "halt":                      # initial opcode for halt instruction
        opcode = 6
        return opcode << 22                                         # shift value to 32-bit
    elif instruction[1].strip('\r\n') == "noop":                    # initial opcode for noop instruction
        opcode = 7
        return opcode << 22                                         # shift value to 32-bit
