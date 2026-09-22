users = [
    {"name" : "atiya", "d_o_b" : "12-2-2010", "e_mail" : "" , "password" : "abc123"},
    {"name" : "ansa" , "d_o_b" : "10-1-2015", "e_mail" : "monno_rajput@gmail.com" , "password" : ""},
    {"name" : "aiman" , "d_o_b" : "04-1-2016", "e_mail" : "aiman_rajput@gmail.com" , "password" : "agsw456" },
    {"name" : "aisha" , "d_o_b" : "05-1-2018", "e_mail" : "" , "password" : "efg789"},
    {"name" : "aliha" , "d_o_b" : "05-8-1996", "e_mail" : "aliha_rajput@gmail.com" , "password" : ""},
    {"name" : "ahana" , "d_o_b" : "05-8-1926", "e_mail" : "ahana_rajput@gmail.com" , "password" : "mnk459"},
]

for user in users:
    if user["password"] == "":
        print(user["name"], "has an", "- invalid password")

for user in users:
    if user["e_mail"] == "":
        print(user["name"], "has an" , "- invalid e_mail")

# i = 1
# while i <= 10:
#     print("hello")
#     i+=1