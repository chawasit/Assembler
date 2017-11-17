import sys
def registor_validator(registor):
    if(registor < 0 or registor > 7):
        sys.exit(1)

def offset_validator(offset):
    if(offset < -32768 or offset > 32767):
        sys.exit(1)
    
def label_isvalid(labels, label):
    if labels.has_key(label) or len(label) > 6:  
        sys.exit(1)
    else:
        return True