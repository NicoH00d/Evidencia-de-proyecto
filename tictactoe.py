"""
Tic Tac Toe Game

Contains functions that draw the tic tac toe grid game and allows
players "X" and "O" to draw on it while keeping game state updated.
"""

from turtle import goto, circle, update, setup, hideturtle, tracer
from turtle import up, down, onscreenclick, done
from freegames import line


def grid():
    """Draw the tic-tac-toe grid lines."""
    line(-67, 200, -67, -200)  # Vertical left line.
    line(67, 200, 67, -200)  # Vertical right line.
    line(-200, -67, 200, -67)  # Horizontal top line.
    line(-200, 67, 200, 67)  # Horizontal bottom line.


def drawx(x, y):
    """Enable Player X to draw an "X" shape in the grid.

    Args:
    x: The x-coordinate of the "X" shape.
    y: The y-coordinate of the "X" shape."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Enable Player O to draw an "O" shape in the grid.

    Args:
    x: The x-coordinate of the "O" shape.
    y: The y-coordinate of the "O" shape."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round a given value down to the grid
    with square size 133 and then subtracts 200.

    Args:
        value: The value to round down.

    Returns:
        The rounded down value subtracted by 200."""
    return ((value + 200) // 133) * 133 - 200


# Initialize the game state with the 'player' set to 0.
state = {'player': 0}


# Create a list containing the functions "drawx" and "drawo".
players = [drawx, drawo]


def tap(x, y):
    """Draw an X or O shape in the square of the grid tapped by the player,
    updating then the game to switch to the next player.

    Args:
        x: The x-coordinate of the tapped square.
        y: The y-coordinate of the tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)  # Sets the size of the game window.
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
