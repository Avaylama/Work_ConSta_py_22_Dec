for i in range(1,4,1):
    userName = input("ENter the username : ")
    password = input("Enter the password ")
    usn = "avay"
    pas = "lama"
    if usn != userName or pas != password:
        if i == 1:
            print("2 attempt left")
            continue
        elif i == 2:
            print("1 attempts left")
            continue
        elif i == 3:
             print("Module blocked")
             break
        else:
            pass
    elif usn == userName or pas == password:
        print("Successfully loggedin")
        break
    else:
        pass


    
        
    
        
    
       
    
        
