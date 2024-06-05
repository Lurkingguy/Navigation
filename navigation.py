import os
import msvcrt

character = "timber"
character_x = 1
character_y = 1

width = 30
height = 30


obstacles = [(10, 15), (5, 20), (20, 10)]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_game():
    clear_screen()
    for y in range(height):
        for x in range(width):
            if (x, y) == (character_x, character_y):
                print(character, end=" ")
            elif (x, y) in obstacles:
                print("yasuo", end=" ")  
            else:
                print("  ", end=" ")
        print()

def get_key():
    return msvcrt.getch().decode("utf-8")

while True:
    display_game()
    key = get_key()

    if key == "w":
        character_y -= 1
    elif key == "s":
        character_y += 1
    elif key == "a":
        character_x -= 1
    elif key == "d":
        character_x += 1
    elif key == "q":
        print("Bye idiot!")
        break

    character_x = max(0, min(character_x, width - 1))
    character_y = max(0, min(character_y, height - 1))


    if (character_x, character_y) in obstacles:
        print("You dead haha!")
        break
