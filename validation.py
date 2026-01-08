#Validates imputs
from window import *
import time

def validate_str(value,options):
    if value in options: return True
    else: return False

def convert_int(value):
    try: return int(value)
    except:
        print("Invaled input!")
        return False
    
def Score(player,computer,rounds):
    if rounds == 0:
        if player > computer: return "Player wins!"
        elif player == computer: return "It's a tie!"
        else: return "Computer wins!"
    print(player,"-",computer)

def wait():
    while choice_entry.get() == "":
        win.update()
        time.sleep(0.1)

def key_press():
    pressed = False

    def set_pressed(): #need a better way of doing this
        nonlocal pressed
        pressed = True

    win.bind("<KeyPress>",lambda event: set_pressed())

    while not pressed:
        win.update()
        time.sleep(0.1)

    clear_window()

    return pressed
