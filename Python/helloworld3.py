def add_to_dict(dict_name,key = "",value = ""):
    print(type(dict_name))
    if type(dict_name) != dict:
        print("You need to send a dictionary. You sent: " + str(type(dict_name)))

my_english_dict = {}
add_to_dict(my_english_dict, "kimchi")