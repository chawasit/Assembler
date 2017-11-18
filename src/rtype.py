import validator
def rtype(instruction):

    # initial opcode and register for each instruction
    opcode = 0 if instruction[1] == "add" else 1                            
    regA = int(instruction[2].strip('\r\n'))
    regB = int(instruction[3].strip('\r\n'))
    rd = int(instruction[4].strip('\r\n'))

    # check if register is valid
    validator.registor_validator(regA)                                      
    validator.registor_validator(regB)
    validator.registor_validator(rd)

    # shift value to 32-bit
    return (opcode << 22) + (regA << 19) + (regB << 16) + rd                