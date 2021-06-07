def str_reverse(words):
    words.reverse()
    print(words)
    
    ## to string
    str = ""
    for x in words:
        str += x
        str += " "
    print(str)
    return str
 
##
words = "AL the Cat"
print(words)
words_as_list = words.split(" ")
lst = str_reverse(words_as_list)