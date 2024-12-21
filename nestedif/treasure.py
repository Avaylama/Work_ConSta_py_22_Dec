print("Welcome to Treasure Land")
direction = input("Choose rigth or left")
if direction == "left":
        choose = input("Choose swim or wait")
        if choose == "wait":
                select = input("Select color")
                if select == "yellow":
                
                        print("You win")
                else:
                        if select in ["red", "blue"]:
                                print("Game Over")
                        
                        
        else:
                if choose == "swim":
                        print("Game Over")
else:
        if direction == "right":
                print("Game Over")
        


