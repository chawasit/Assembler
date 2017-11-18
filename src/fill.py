def fill(instruction, labels):
    try:
        
        # check if offset value is integer                                                                
        return int(instruction[2].strip('\r\n'))
    
    except:

        # offset value is not interger                                                             
        return labels[instruction[2].strip('\r\n')]