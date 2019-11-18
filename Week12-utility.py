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
    


