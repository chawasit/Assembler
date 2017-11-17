import validator
def jtype(instruction):
    opcode = 5
    regA = int(instruction[2].strip('\n'))
    regB = int(instruction[3].strip('\n'))

    validator.registor_validator(regA)
    validator.registor_validator(regB)

    return (opcode << 22) + (regA << 19) + (regB << 16)