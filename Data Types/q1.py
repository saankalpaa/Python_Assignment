str = input('enter the string')

def char_freq(str):
    dict={}
    for i in str:
        keys= dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
    
print(char_freq(str))        

