import os
import math


PLANE_WIDTH = 100
PLANE_LENGTH = 200
PLAIN_PLANE = [[' ' for _ in range(PLANE_LENGTH)] for _ in range(PLANE_WIDTH)]

CENTERX, CENTERY = PLANE_LENGTH // 2, PLANE_WIDTH // 2

POINTS = []
NEW_POINTS = []


def initialize_square():
    STARTX, ENDX = 10, 20
    STARTY, ENDY = 5, 15
    for y in range(STARTY, STARTY+ENDY):
        for x in range(STARTX, STARTX+ENDX):
            if (y == STARTY or y == STARTY+ENDY-1 or x == STARTX or x == STARTX+ENDX-1):
                POINTS.append((y, x))


def initialize_line(M: float = 1, C=0):
    for y in range(PLANE_LENGTH):
        for x in range(PLANE_WIDTH):
            if y == int(M*x + C):
                POINTS.append((y, x))


def draw_plane():
    for str_arr in PLAIN_PLANE:
        print(''.join(str_arr))


def clear_plane():
    for (y, x) in NEW_POINTS:
        PLAIN_PLANE[y][x] = ' '


def rotate_points(angle):
    for idx in range(len(POINTS)):
        y, x = POINTS[idx]
        rad_angle = math.radians(angle)
        x -= CENTERX
        y -= CENTERY
        new_x = int(x * math.cos(rad_angle) - y *
                    math.sin(rad_angle)) + CENTERX
        new_y = int(y * math.cos(rad_angle) + x *
                    math.sin(rad_angle)) + CENTERY
        if 0 <= new_x < PLANE_LENGTH and 0 <= new_y < PLANE_WIDTH:
            PLAIN_PLANE[new_y][new_x] = '.'
            NEW_POINTS.append((new_y, new_x))


def initialize_points():
    SQUARE_WIDTH = 12
    SQUARE_LENGTH = 18
    for c in range(-PLANE_LENGTH, PLANE_LENGTH, SQUARE_WIDTH):
        initialize_line(1, c)
    for c in range(0, PLANE_LENGTH * 2, SQUARE_LENGTH):
        initialize_line(-1, c)


def main(angle=0):
    rotate_points(angle)
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
