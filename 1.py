count = input("Please Enter User Count :")
users = []
for x in range(0,int(count)) :
     
    user_data = {}    
    user_data["Name"] = input("Enter user name : ")
    user_data["Age"] = input("Enter user age : ")

    users.append(user_data)

search = input("Please Enter a name to search :")  

for res in users :
    if res['Name'] == search :
       print(res['Age'])
       break
    else :
       print("There is no user with given name !")
       
