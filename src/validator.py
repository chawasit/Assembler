import sys
def registor_validator(registor):                                   # check if register is valid
    if(registor < 0 or registor > 7):
        sys.exit("invalid register")

def offset_validator(offset):                                       # check if offset is valid
    if(offset < -32768 or offset > 32767):
        sys.exit("invalid offset")
    
def label_isvalid(labels, label):                                   # check if labels, label is valid
    if labels.has_key(label):
        sys.exit("dupicate label")
    elif len(label) > 6:  
        sys.exit("exceed 6 characters label")
    elif label[0] >= "0" and label[0] <= "9":
        sys.exit("1st character is number")
    else:
        return True