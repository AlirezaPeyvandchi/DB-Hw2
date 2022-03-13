count = input("Please Enter User Count :")
users = []
for x in range(0,int(count)) :
     
    user_data = {}    
    user_data["Name"] = input("Enter user name : ")
    user_data["Age"] = input("Enter user age : ")

    users.append(user_data)

search = input("Please Enter a name to search :")  
found=False
for res in users :
    if res['Name'] == search :
       found=True
       print(res['Age'])
       break
          
if found==False:
     print("There is no user with given name !")
       
