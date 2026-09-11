import numpy as np


WIDTH = 2000
HEIGHT = 2000

TOTAL_TIME = 20

DT = 0.01


MIN_SPEED = 50
MAX_SPEED = 1000

MAX_DIRECTION_CHANGE = np.pi / 10


def generate_trajectory():

    n = int(TOTAL_TIME / DT)

    x = np.zeros(n)
    y = np.zeros(n)

    speed = np.zeros(n)


    x[0] = np.random.uniform(0, WIDTH)
    y[0] = np.random.uniform(0, HEIGHT)


    speed[0] = np.random.uniform(MIN_SPEED, MAX_SPEED)


    theta = np.random.uniform(0, 2 * np.pi)


    for i in range(1, n):

        # Randomly change direction
        theta += np.random.uniform(
            -MAX_DIRECTION_CHANGE,
            MAX_DIRECTION_CHANGE
        )

        speed[i] = np.random.uniform(
            MIN_SPEED,
            MAX_SPEED
        )

        vx = speed[i] * np.cos(theta)
        vy = speed[i] * np.sin(theta)

        new_x = x[i - 1] + vx * DT
        new_y = y[i - 1] + vy * DT


        if new_x < 0 or new_x > WIDTH:

            vx = -vx
            theta = np.pi - theta

            new_x = x[i - 1] + vx * DT


        if new_y < 0 or new_y > HEIGHT:

            vy = -vy
            theta = -theta

            new_y = y[i - 1] + vy * DT

        new_x = np.clip(new_x, 0, WIDTH)
        new_y = np.clip(new_y, 0, HEIGHT)

        # Store position
        x[i] = new_x
        y[i] = new_y

    return x, y, speed
