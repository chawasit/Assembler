#!/usr/bin/python

def otype(instruction,labels):

    # initial opcode for halt instruction
    if instruction[1].strip('\r\n') == "halt":                      
        opcode = 6

        # shift value to 32-bit
        return opcode << 22

    # initial opcode for noop instruction                                             
    elif instruction[1].strip('\r\n') == "noop":                    
        opcode = 7

        # shift value to 32-bit
        return opcode << 22                                         
