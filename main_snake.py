import tkinter
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 40
SPACE_SIZE = 40
BODY_SPACING = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = 'FF0000'
BACKGROUND = '000000'




class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

def run():
    window = tkinter.Tk()
    window.title('Snake Game')
    window.resizable(False, False)

    score = 0
    direction = 'down'
    score_label = tkinter.Label(window, text="Score: {}".format(score), font=('consolas', 40))
    score_label.pack()




    window.mainloop()

if __name__ == '__main__':
    run()
