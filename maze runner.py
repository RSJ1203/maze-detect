"""
Project:maze runner
"""



from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def right_is_clear():
    turn_right()
    if front_is_clear():
        turn_left()
        return True
    turn_left()
    return False
def main():
    while not on_beeper():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
if __name__ == '__main__':
    execute_karel_task(main)