def rtype(instruction):
    print instruction
    opcode = 0 if instruction[1] == "add" else 1
    regA = int(instruction[2])
    regB = int(instruction[3])
    rd = int(instruction[4])
    return (opcode << 22) + (regA << 19) + (regB << 16) + rd