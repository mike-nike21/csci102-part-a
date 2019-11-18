# Github Repo
# Michael Ortega
# CSCI 102 - Section E
# Week 11 - Part B

# PrintOutput Function

def PrintOutput(string):
    print('OUTPUT',string)

# LoadFile Function

def LoadFile(file_name):
    open_file = open(file_name, 'r')
    contents = open_file.read().split('\n')
    open_file.close()
    return contents

# UpdateString Function

def UpdateString(string_1, string_2, i):
    list_form = list(string_1)
    list_form[i] = string_2
    output = ''
    for letter in list_form:
        output += letter
    PrintOutput(output)
    
# FindWordCount Function

def FindWordCount(ls, string_1):
    count = 0
    new_list = ''
    for i in ls:
        for j in i:
            new_list += j
        final_list = new_list.split()
        for i in final_list:
            if i == string_1:
                count += 1
    return count

