import tkinter
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 70
SPACE_SIZE = 25
BODY_SPACING = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND = '#000000'


class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_SPACING
        self.coordinates = []
        self.squares = []

        for i in range(BODY_SPACING):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)

    def get_coordinates(self):
        return self.coordinates

    def insert_coordinates(self, index, value):
        self.coordinates.insert(index, value)

    def get_squares(self):
        return self.squares

    def insert_square(self, index, value):
        self.squares.insert(index, value)

    def delete_square(self,value):
        del self.squares[value]

class Food:
    def __init__(self, canvas):
        flag = False
        while True:
            x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE
            for value in snake.get_coordinates():
                if x == value[0] and y == value[1]:
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
        self.coordinates = (x,y)
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag= 'food')

    def get_coordinates(self):
        return self.coordinates

def next_turn(snake, food):
    x,y = snake.get_coordinates()[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    else:
        x += SPACE_SIZE

    snake.insert_coordinates(0, (x,y))

    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y + SPACE_SIZE, fill=SNAKE_COLOR, )
    snake.insert_square(0, square)

    if x == food.get_coordinates()[0] and y == food.get_coordinates()[1]:
        global score

        score += 1
        score_label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food(canvas)

    else:

        del snake.coordinates[-1]
        canvas.delete(snake.get_squares()[-1])
        snake.delete_square(-1)

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    else:
        if direction != 'up':
            direction = new_direction


def check_collision(snake):
    x, y = snake.get_coordinates()[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body in snake.get_coordinates()[1:]:
        if x == body[0] and y == body[1]:
            return True

    return False

def game_over():
    canvas.delete(tkinter.ALL)
    canvas.create_text(window_width/2, window_height/2, font=('consolas', 70), text = "GAME OVER", fill = "red", tag = "GameOver")


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

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))

snake = Snake(canvas)
food = Food(canvas)
next_turn(snake, food)

window.mainloop()


