"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""


def add_to_dict(dict_name,key = "",value = ""):
    
    if type(dict_name) != dict:
        print("You need to send a dictionary. You sent: " + str(type(dict_name)))
        
    elif key == "" or value =="":
        print("You need to send a word and a definition")
    
    elif key in dict_name:
        print(key + " is already on the dictionary. Won't add")
    
    else:
        dict_name[key] = value
        print(key + " has been added")

def get_from_dict(dict_name,key = ""):
    if type(dict_name) != dict:
        print("You need to send a dictionary. You sent: " + str(type(dict_name)))

    elif key == "":
        print("You need to send a word to search for")

    elif key in dict_name:
        print(key + ": " +dict_name[key])
    
    else:
        print(key + "was not found in this dict")

def update_word(dict_name,key = "",value = ""):
    if type(dict_name) != dict:
        print("You need to send a dictionary. You sent: " + str(type(dict_name)))

    elif key == "" or value =="":
        print("You need to send a word and a definition to update")
    
    elif key in dict_name:
        dict_name[key] = value
        print(key + " has been updated to: " +value)

    else:
        print(key + " is not found in this dict. Can't update non-existing word")

def delete_from_dict(dict_name,key = ""):
    if type(dict_name) != dict:
        print("You need to send a dictionary. You sent: " + str(type(dict_name)))

    elif key == "":
        print("You need to specify a word to delete")
    
    elif key in dict_name:
        del dict_name[key]
        print(key + " has been deleted")

    else:
        print(key + " was not found in this dict. Won't delete")

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('cls')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\