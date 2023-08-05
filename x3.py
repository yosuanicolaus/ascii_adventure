import os
import math


PLANE_WIDTH_Y = 45
PLANE_LENGTH_X = 200
CANVAS_Y_X = [[' ' for _ in range(PLANE_LENGTH_X)]
              for _ in range(PLANE_WIDTH_Y)]

CENTERX, CENTERY = PLANE_LENGTH_X // 2, PLANE_WIDTH_Y // 2

POINTS = []
NEW_POINTS_Y_X = []


def create_border():
    for x in range(PLANE_LENGTH_X):
        CANVAS_Y_X[0][x] = '#'
        CANVAS_Y_X[PLANE_WIDTH_Y-1][x] = '#'
    for y in range(PLANE_WIDTH_Y):
        CANVAS_Y_X[y][0] = '#'
        CANVAS_Y_X[y][PLANE_LENGTH_X-1] = '#'


def initialize_square():
    STARTX, ENDX = 10, 20
    STARTY, ENDY = 5, 15
    for y in range(STARTY, STARTY+ENDY):
        for x in range(STARTX, STARTX+ENDX):
            if (y == STARTY or y == STARTY+ENDY-1 or x == STARTX or x == STARTX+ENDX-1):
                POINTS.append((y, x))


def initialize_line(M: float = 1, C=0):
    for y in range(PLANE_LENGTH_X):
        for x in range(PLANE_LENGTH_X):
            if y == int(M*x + C):
                POINTS.append((y, x))


def draw_plane():
    for str_arr in CANVAS_Y_X:
        print(''.join(str_arr))


def clear_plane():
    for (y, x) in NEW_POINTS_Y_X:
        CANVAS_Y_X[y][x] = ' '


def rotate_points(angle):
    for idx in range(len(POINTS)):
        y, x = POINTS[idx]
        rad_angle = math.radians(angle)
        y -= CENTERY
        x -= CENTERX
        new_y = int(y * math.cos(rad_angle) + x *
                    math.sin(rad_angle)) + CENTERY
        new_x = int(x * math.cos(rad_angle) - y *
                    math.sin(rad_angle)) + CENTERX
        if 0 <= new_x < PLANE_LENGTH_X and 0 <= new_y < PLANE_WIDTH_Y:
            CANVAS_Y_X[new_y][new_x] = '.'
            NEW_POINTS_Y_X.append((new_y, new_x))


def initialize_points():
    SQUARE_WIDTH_Y = 10
    SQUARE_LENGTH_X = 10
    for c in range(-PLANE_LENGTH_X, PLANE_LENGTH_X, SQUARE_LENGTH_X):
        initialize_line(1, c)
    for c in range(0, PLANE_LENGTH_X * 2, SQUARE_WIDTH_Y):
        initialize_line(-1, c)


def main(angle=0):
    rotate_points(angle)
    create_border()
    draw_plane()
    clear_plane()


if __name__ == "__main__":
    angle = 0
    initialize_points()

    while (True):
        os.system('clear')
        main(angle)
        # time.sleep(0.05)
        inp = input()
        multiplier = int(inp[:-1]) if len(inp) > 1 else 1
        if inp[-1:] == 'q':
            angle -= 6 * multiplier
            while angle < 0:
                angle += 360
        elif inp[-1:] == 'e':
            angle += 6 * multiplier
        else:
            continue
        angle %= 360
