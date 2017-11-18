def fill(instruction, labels):
    try:

        # check if offset value numeric                                                                
        return int(instruction[2].strip('\r\n'))
    
    except:

        # offset value is symbolic                                                             
        return labels[instruction[2].strip('\r\n')]