#!/usr/bin/python2
def i_type(instruction,labels,index):
    if instruction[1] == 'lw':
        op = 2
    elif instruction[1] == 'sw':
        op = 3
    elif instruction[1] == 'beq':
        op = 4
    rs = int(instruction[2].strip('\n'))
    rt = int(instruction[3].strip('\n'))
    try:
        offset = int(instruction[4].strip('\n'))
    except:
        offset = -index + 1
    return (op << 22) + (rs << 19) + (rt << 16) + (offset & 0xffff)
