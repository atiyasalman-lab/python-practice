question = input("Do you want to add, delete, read , update? ")
names = ["atya" , "ansa" , "sadka"]
if question == "add":
    new_name = input("what will be the new name? : ")
    names.append(new_name)
    print(names)
    
elif question == "read":
    name_to_read = int(input("which index you want to read? "))
    print(names[name_to_read])
    
elif question == "update":
    old_name = input("which name you want to update? ")
    new_name = input("Enter new name? ")
    index = names.index(old_name)
    names[index] = new_name
   
    print(names)

else:
    remove_name = input("what will be the name for removing? ")
    index_of_remove_name = names.index(remove_name)
    names.pop(index_of_remove_name)
    print(names)


    
# elif question == "update" :
#     Ques1 = input("which name you want to update? ")
#     Ques2 = input("Enter new name? ")
#     index = names.index(Ques1)
#     names[index] = Ques2
#     print

#     print(names)

