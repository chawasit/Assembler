#!/usr/bin/python2


<<<<<<< Updated upstream
def i_type(instruction,labels):
=======
def i_type(instruction,labels,index):
>>>>>>> Stashed changes
    if instruction[1] == 'lw':
        op = 2
    elif instruction[1] == 'sw':
        op = 3
    elif instruction[1] == 'beq':
        op = 4

<<<<<<< Updated upstream
    rs = int(instruction[2])
    rt = int(instruction[3])
    try:
        offset = int(instruction[4])
    except:
        offset = labels[instruction[4]]
=======
    rs = int(instruction[2].strip('\n'))
    rt = int(instruction[3].strip('\n'))

    try:
        offset = int(instruction[4].strip('\n'))
    except:
        offset = -index + 1

>>>>>>> Stashed changes
    return (op << 22) + (rs << 19) + (rt << 16) + (offset & 0xffff)
