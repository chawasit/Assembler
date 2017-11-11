#!/usr/bin/python2


def i_type(instruction,labels):
    if instruction[1] == 'lw':
        op = 2
    elif instruction[1] == 'sw':
        op = 3
    elif instruction[1] == 'beq':
        op = 4

    rs = int(instruction[2])
    rt = int(instruction[3])
    try:
        offset = int(instruction[4])
    except:
        offset = labels[instruction[4]]
    return (op << 22) + (rs << 19) + (rt << 16) + (offset & 0xffff)
