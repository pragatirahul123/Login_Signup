import json
Exits=""
user_input=input("login or signup : ")
def write_json(data,file="userdetails.json"):
    with open(file,"w")as f:
        json.dump(data,f)

if user_input == "login":
    username=input("username")
    password=input("password")
    with open("userdetails.json") as f:
        var = json.load(f)
        var2 = var["userdetails"]
        #print("var2",var2)
        for k in var2:
            if k["username"]==username and k["password"]==password:
                print("you are login successful")
                print("this is"+k["username"]+",and my date of birth is"+ k["profile"]["dob"]+"and gender is"+k["profile"]["gender"])
                break
            else:
                print("invalid password/username")
                break
elif user_input =="signup":
    username=input("username:")
    password1=input("password :")
    password2=input("confirm password :")
    if password1!=password2:
        print("both password not same")

    else:
        with open('userdetails.json') as json_file:
            data=json.load(json_file)
            temp = data["userdetails"]
            for i in temp:
                
                if i["username"]== username:
                    Exits="yes"
            if Exits== "yes":
                print(username,"username is already exits")
            elif Exits == "":
                print("you are signup successfully")
                description=input("description :")
                date_of_birth =input("DOB :")
                hobbies= input("hobbies : ")
                gender= input("gender:")
                dic={"username":username,"password":password1,"profile":{"description":description,"dob":date_of_birth,"hobbies":hobbies}}
                temp.append(dic)
                print("username :", username)
                print("gender :",gender)
                print("bio: i am mona")
                print("hobbies:",hobbies)
                print("dob:",date_of_birth)

                write_json(data)
                




