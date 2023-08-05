import os
import math
import time


PLANE_WIDTH = 50
PLANE_LENGTH = 100
PLAIN_PLANE = [[' ' for _ in range(PLANE_LENGTH)] for _ in range(PLANE_WIDTH)]

STARTX, ENDX = 10, 20
STARTY, ENDY = 5, 15
CENTERX, CENTERY = PLANE_LENGTH // 2, PLANE_WIDTH // 2

POINTS = []
NEW_POINTS = []


def initialize_points():
    for x in range(STARTX, STARTX+ENDX):
        for y in range(STARTY, STARTY+ENDY):
            if (y == STARTY or y == STARTY+ENDY-1 or x == STARTX or x == STARTX+ENDX-1):
                POINTS.append((x, y))


def draw_plane():
    for str_arr in PLAIN_PLANE:
        print(''.join(str_arr))


def clear_plane():
    for (x, y) in NEW_POINTS:
        PLAIN_PLANE[y][x] = ' '


def main(angle=0):
    for idx in range(len(POINTS)):
        x, y = POINTS[idx]
        rad_angle = math.radians(angle)
        x -= CENTERX
        y -= CENTERY
        new_x = int(x * math.cos(rad_angle) - y *
                    math.sin(rad_angle)) + CENTERX
        new_y = int(y * math.cos(rad_angle) + x *
                    math.sin(rad_angle)) + CENTERY
        if 0 <= new_x < PLANE_LENGTH and 0 <= new_y < PLANE_WIDTH:
            PLAIN_PLANE[new_y][new_x] = '@'
            NEW_POINTS.append((new_x, new_y))

    draw_plane()
    clear_plane()


if __name__ == "__main__":
    angle = 0
    initialize_points()
    while (True):
        os.system('clear')
        main(angle)
        time.sleep(0.05)
        angle += 6
        angle %= 360
