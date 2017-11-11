def rtype(instruction):
    opcode = 0 if instruction[1] == "add" else 1
    regA = int(instruction[2].strip('\n'))
    regB = int(instruction[3].strip('\n'))
    rd = int(instruction[4].strip('\n'))
    return (opcode << 22) + (regA << 19) + (regB << 16) + rd