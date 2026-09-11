import random
from manim import *

from beacon import create_beacon
from motion import (
    square_path,
    circle_path,
    figure8_path,
    straight_path,
    random_path
)


class BeaconGenerator(Scene):

    def construct(self):

        beacon = create_beacon()
        self.add(beacon)

        paths = [
            straight_path,
            square_path,
            circle_path,
            figure8_path,
            random_path
        ]

        selected_path = random.choice(paths)
        # selected_path = figure8_path
        # selected_path = square_path
        # selected_path = circle_path
        selected_path = straight_path

        path, speed = selected_path()

        beacon.move_to(path.get_start())

        t = 5
        while(t > 0):
            self.play(
                MoveAlongPath(
                    beacon,
                    path
                ),
                run_time=speed,
                rate_func=linear
            )
            t = t - 1