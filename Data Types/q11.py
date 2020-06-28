str = input('enter the string')

def word_freq(str):
    dict={}
    words = str.split()
    
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
    
print(word_freq(str))  