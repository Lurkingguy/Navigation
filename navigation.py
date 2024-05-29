import os
import msvcrt    # Cái thư viện giúp m read keyboard


character = "timber"
character_x = 1                          # Starting point
character_y = 1 

width = 15                                                          #Endcoding the navigation 
height = 25


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")                # Dùng cái này để clean background


def display_game():
    clear_screen()
    for y in range(height):
        for x in range(width):                                         # End moving nếu character chạm đáy xã hội :D
            if x == character_x and y == character_y:
                print(character, end=" ")
            else:
                print("....", end=" ")
        print()


def get_key():
    return msvcrt.getch().decode("utf-8")               # Thao tác keyboard by using a.w.s.d 


while True:
    display_game()
    key = get_key()                  # get key đây nè

    if key == "w":
        character_y -= 1
    elif key == "s":
        character_y += 1
    elif key == "a":
        character_x -= 1
    elif key == "d":
        character_x += 1
    elif key == "q":
        print("Goodbye!")
        break


    character_x = max(0, min(character_x, width - 1))
    character_y = max(0, min(character_y, height - 1))
