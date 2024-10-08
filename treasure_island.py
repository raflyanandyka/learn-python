print("Welcome to Treasure Island Game")
print("Your mission is to find treasure")
menu = input("You found a crossroads!\n\tPlease choose \"left\" or \"Right\"\n>>>> ")
if menu != "left":
    print("Oops... You fall into a hole!")
    print("Game Over")
else:
    menu = input("You arrive at the harbor\n\tPlease choose \"swim\" \"wait\"\n>>>> ")

    if menu != "wait":
        print("Oops... You got attacked by a trout!")
        print("Game Over")
    else:
        menu = input("You arrive at the island and found three doors\n\tPlease choose \"red\" \"yellow\" \"blue\"\n>>>> ")
        if menu == "red":
            print("Oops... you are burned by fire!")
            print("Game Over")
        elif menu == "blue":
            print("Oops... you are eaten by beasts!")
            print("Game Over")
        else:
            print("You found the treasure")
            print("You Win")
