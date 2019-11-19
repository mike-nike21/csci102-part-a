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

# ScoreFinder Function

def ScoreFinder(ls_1,ls_2,string_1):
    new_player = string_1.lower()
    lower_list = []
    for player in ls_1:
        lower_list.append(player.lower())
    if new_player in lower_list:
        for i in lower_list:
            i = lower_list.index(new_player)
        print('OUTPUT', string_1, 'got a score of', ls_2[i])
    else:
        print('OUTPUT player not found')

# Union Function

def Union(ls_1,ls_2):
    final_list = []
    for word in ls_1:
        if word not in final_list:
            final_list.append(word)
    for words in ls_2:
        if words not in final_list:
            final_list.append(words)
    return final_list

# Intersection Function

def Intersection(ls_1,ls_2):
    middle_list = []
    final_list = []
    for word in ls_1:
        if word in ls_2:
            middle_list.append(word)
    for words in ls_2:
        if words in ls_1:
            middle_list.append(words)
    for dupe in middle_list:
        if dupe not in final_list:
            final_list.append(dupe)
    return final_list

# NotIn Function

def NotIn(ls_1,ls_2):
    final_list = []
    for word in ls_1:
        if word not in ls_2:
            final_list.append(word)
    return final_list






    
    
                

