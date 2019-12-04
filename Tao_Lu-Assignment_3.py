# This is main file of assignment 3

import csv
import assignment_fileRW

### Create list for both clean names and invalid names as global
### clean_list = [] - list for clean names 
### invalid_list = [] - list for invalid names
clean_list = []
invalid_list = []

### Function for seperation names
### Seprate clean names and invalid names, put them into different list

def seperation_list(list):
    for item in dirty_list:
        # if name contian all alpha, add to clean
        if item.isalpha() == True:
                clean_list.append(item)
        else:
            item_len = len(item)
            count = item.count("-")
            # if name has 2 and above "-" or no "-", add to invalid
            if (count != 1):
                invalid_list.append(item)
            # if name has "-" as first letter or last letter, add to invalid
            elif item.find("-") == 0 or item.find("-") == item_len-1:
                invalid_list.append(item)
            else:
                temp_item = item.replace('-','')
                # if name has only alpha and one "-" in between, add to clean
                if temp_item.isalpha() == True:
                    clean_list.append(item)
                # remianing names add to invaid
                else:
                    invalid_list.append(item)

# Test only    
# print(dirty_list)
# print(invalid_list)
# print(clean_list)

### Function for Converting Clean names 
### Convert clean names to uppercase first letter followed by lowercase letters.
### If a name is hyphenated, the name after the hyphen should also start with an upper case letter.

def covertion_list(list):
    clean_len = len(clean_list)
    count = 0
    print(clean_len) # for test
    for item in clean_list:
        location = item.find("-")
        # if name does not have '-'
        if(location == -1):
            clean_list[count] = item.capitalize()
        else:
            # Temporary seperate name in two word by '-'
            temp_item = item.replace('-',' ')
            temp_item = temp_item.title()
            clean_list[count] = temp_item.replace(' ','-')
        count += 1

### Main 
### Open Dirtyname.csv file and read them into list

try:
    dirty_list = assignment_fileRW.file_reader("DirtyNames.csv")

    file_name_count = len(dirty_list)
    print(file_name_count) # for test

    seperation_list(dirty_list)
    covertion_list(clean_list)

    ### Write clean_list and invalid_list in files
    ### CleanNames.csv - clean_list
    ### InvalidNames.csv - invalid_list

    assignment_fileRW.file_writer("CleanNames.csv", clean_list)
    assignment_fileRW.file_writer("InvalidNames.csv", invalid_list)
except:
    print("No such file or directory")





