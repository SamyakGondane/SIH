import numpy as np
from manim import *

rng = np.random.default_rng()


def square_path():

    length = rng.uniform(1, 5)
    speed = rng.uniform(1, 3)

    path = Square(side_length=length)

    return path, speed


def circle_path():

    radius = rng.uniform(1, 5)
    speed = rng.uniform(1, 3)

    path = Circle(radius=radius)

    return path, speed


def figure8_path():

    length_x = rng.uniform(2, 5)
    length_y = rng.uniform(1, 4)

    speed = rng.uniform(1, 3)

    path = ParametricFunction(
        lambda t: np.array([
            length_x * np.sin(t),
            length_y * np.sin(t) * np.cos(t),
            0
        ]),
        t_range=[0, TAU]
    )

    return path, speed


def straight_path():

    start_x = rng.uniform(-5,5)
    start_y = rng.uniform(-5,5)

    end_x = rng.uniform(-5,5)
    end_y = rng.uniform(-5,5)

    speed = rng.uniform(1, 3)

    path = Line(
        start=np.array([start_x, start_y, 0]),
        end=np.array([end_x, end_y, 0])
    )

    return path, speed


def random_path():
    pass