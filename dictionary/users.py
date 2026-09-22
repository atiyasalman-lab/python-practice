users = [
    {"name" : "atiya", "d_o_b" : "12-2-2010", "e_mail" : "ansa_rajput@gmail.com" , "password" : "abc123"},
    {"name" : "ansa" , "d_o_b" : "10-1-2015", "e_mail" : "monno_rajput@gmail.com" , "password" : "123abc"},
    {"name" : "aiman" , "d_o_b" : "04-1-2016", "e_mail" : "aiman_rajput@gmail.com" , "password" : "efg456" },
    {"name" : "aisha" , "d_o_b" : "05-1-2018", "e_mail" : "aisha_rajput@gmail.com" , "password" : "efg789"},
]

Question = input("Do you want to add, delete , update or read: ")
if Question == "add":
    new_name = input("Enter the new_name: ")
    new_dob = input("Enter the new dob: ")
    new_email = input("Enter the new e_mail:  ")
    new_pss = input("Enter the new password: ")
    index = int(input("Enter the index number: "))
    # users.append({"name" : new_name , "d_o_b" : new_dob, "e_mail" : new_email , "password" : new_pss})
    users.insert(index, {"name" : new_name , "d_o_b" : new_dob, "e_mail" : new_email , "password" : new_pss})
    print("Sorry, this index is not defined")
elif Question == "delete":
    removing_name = int(input("Enter the index to delete: "))
    users.pop(removing_name)
elif Question == "read":
    name_to_read = int(input("Enter the index to read: "))
    print(users[name_to_read])
else :
    name_to_update = int(input("Enter the index to update: "))
    which_element = input("Which element want to update name/ d_o_b/ e_mail/ password? ")
    new_update = input("what to update in this element? ")
    users[name_to_update][which_element] = new_update

# for user in users:
#     print(user)
