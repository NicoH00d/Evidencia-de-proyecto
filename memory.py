"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import shuffle
from turtle import (addshape, begin_fill, clear, color, done, down,
                    end_fill, forward, goto, hideturtle, left, onscreenclick,
                    ontimer, setup, shape, stamp, tracer, up, update, write)

from freegames import path

"""Set the car image revealed by playing as a variable."""
car = path('car.gif')
"""Populate the 8x8 grid with two sets of numbers up to 32."""
tiles = list(range(32)) * 2
"""Define mark as having a null value so no tiles appear as clicked."""
state = {'mark': None}
"""Set value hide to True so images start hidden."""
hide = [True] * 64
tap_count = 0
match_count = 0


def square(x, y):
    """Receives: x and y integer values.
    Draws a white square with black outline at (x, y).
    This creates the grid to hide the picture.
    """
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Receives: x and y integer values.
    Converts (x, y) coordinates to tiles index.
    Used to locate specific tiles in the program.
    """
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Receives: count integer value.
    Converts tiles count to (x, y) coordinates.
    """
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Receives: x and y integer values.
    Update mark and hidden tiles based on tap.
    """
    global tap_count
    tap_count = tap_count + 1
    spot = index(x, y)
    mark = state['mark']

    """If the user clicks tiles that do not match, it resets the tile.
    Else, if the tiles match, it reveals the image beneath.
    """
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        tap_count = tap_count + 1
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global match_count
        match_count = match_count +1


def draw():
    """Draw image (car picture)."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    """Draw tiles (squares covering the picture)."""
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    """If a blank tile is clicked, it prints the number of the tile."""
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
print("You tapped", tap_count, "times")
print("You completed", match_count, "matches")
if (match_count == 32):
    print("You completed all the matches!")
