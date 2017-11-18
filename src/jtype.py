import validator
def jtype(instruction):

    # initial opcode and register for each instruction                                                  
    opcode = 5
    regA = int(instruction[2].strip('\r\n'))
    regB = int(instruction[3].strip('\r\n'))

    # check if register is valid
    validator.registor_validator(regA)                                  
    validator.registor_validator(regB)

    # shift value to 32-bit
    return (opcode << 22) + (regA << 19) + (regB << 16)                 