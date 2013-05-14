import string

input_str = raw_input()
lower_set = set(string.ascii_lowercase)
upper_set = set(string.ascii_uppercase)

def situation_one(input_str): 
    if len(input_str) == 1 and input_str[0] in lower_set:
        return True
    flag = False
    if input_str[0] in lower_set: 
        for letter in input_str[1:]:
            if letter in upper_set:
                flag = True
            else:
                flag = False 
                break
    return flag


def situation_two(input_str):
    flag = False
    for letter in input_str:
        if letter in upper_set:
            flag = True
        else:
            flag = False
            break
    return flag

if situation_one(input_str):
    print input_str[0].upper() + input_str[1:].lower()
elif situation_two(input_str):
    print input_str.lower()
else:
    print input_str
    
