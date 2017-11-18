#!/usr/bin/python2
import validator
def i_type(instruction,labels,index):

    # initial opcode and register for each instruction                                       
    if instruction[1] == 'lw':                                                     
        op = 2
    elif instruction[1] == 'sw':
        op = 3
    elif instruction[1] == 'beq':
        op = 4

    # throw exception    
    if int(instruction[2].strip('\n')) > 7:                                 
        raise ValueError("Arrays must have the same size")
    else:
        rs = int(instruction[2].strip('\n'))
    rt = int(instruction[3].strip('\n'))
    try:

        # check if offset value is numeric                                                                    
        offset = int(instruction[4].strip('\n'))
    except:

        # offset value is symbolic                                                                 
        offset = labels[instruction[4].strip('\n')]
        if instruction[1] == 'beq':
            offset -= index + 1

    # check if register is valid        
    validator.registor_validator(rs)                                        
    validator.registor_validator(rt)                                        
    validator.offset_validator(offset)

    # shift value to 32-bit
    return (op << 22) + (rs << 19) + (rt << 16) + (offset & 0xffff)        
