import curses
from random import randint 

def main(win):
    win = curses.newwin(20,60,0,0)

    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    snake = [(4,10), (4,9), (4,8)]
    food = (10,20)
    bounds_y = (0,19)
    bounds_x = (0,59)

    allowed_moves = (curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN)

    opposite_moves = {
        curses.KEY_LEFT, curses.KEY_RIGHT,
        curses.KEY_RIGHT, curses.KEY_LEFT,
        curses.KEY_UP, curses.KEY_DOWN,
        curses.KEY_DOWN, curses.KEY_UP
    }

    win.addch(food[0], food[1], '*')

    score = 0
    ESC = 27
    key = curses.KEY_RIGHT

    while key != ESC:
        win.addstr(0, 2, f'Score: {score} ')
        win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

        prev_key = key
        event = win.getch()
        key = event if event in allowed_moves else prev_key
        
        if event in allowed_moves:
            if opposite_moves[key] != prev_key:
                key = event
            else:
                key = prev_key

        y = snake[0][0] #head piece (starts at y instead of x)
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -=1
        if key == curses.KEY_RIGHT:
            x +=1

        snake.insert(0, (y,x))

        if y in bounds_y or x in bounds_x or snake[0] in snake[1:]:
            print(f"Game Over, Your Score was {score}")
            break 

        if snake[0] == food:
            score += 1
            food = ()
            while food == ():
                food = (randint(bounds_y[0]+1, bounds_y[1]-1), randint(bounds_x[0]+1, bounds_x[1]-1))
                if food in snake:
                    food = ()
            win.addch(food[0], food[1], '*')
        else:
            last = snake.pop()

        win.addch(snake[0][0], snake[0][1], '#')



curses.wrapper(main)