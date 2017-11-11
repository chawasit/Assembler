def fill(instruction, labels):
    try:
        return int(instruction[2].strip('\n'))
    except:
        return labels[instruction[2].strip('\n')]