import tkinter
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 40
SPACE_SIZE = 40
BODY_SPACING = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND = '#000000'




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

    canvas = tkinter.Canvas(window, bg = BACKGROUND, width=GAME_WIDTH, height= GAME_HEIGHT)
    canvas.pack()

    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_axis = int((screen_width / 2) - (window_width / 2))
    y_axis = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x_axis}+{y_axis}")

    window.mainloop()

if __name__ == '__main__':
    run()
