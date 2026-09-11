import numpy as np
from manim import *

from beacon import create_beacon
from motion import (
    generate_trajectory,
    WIDTH,
    HEIGHT,
    TOTAL_TIME,
    DT
)


config.frame_rate = 30


class BeaconGenerator(Scene):

    def construct(self):

        x, y, speed = generate_trajectory()

        beacon = create_beacon()
        self.add(beacon)


        def pixel_to_manim(px, py):

            return np.array([
                (px / WIDTH) * config.frame_width
                - config.frame_width / 2,

                (py / HEIGHT) * config.frame_height
                - config.frame_height / 2,

                0
            ])

        beacon.move_to(
            pixel_to_manim(x[0], y[0])
        )

        points = []

        for i in range(len(x)):

            points.append(
                pixel_to_manim(x[i], y[i])
            )

        trajectory = VMobject()

        trajectory.set_points_as_corners(points)

        self.play(
            MoveAlongPath(
                beacon,
                trajectory
            ),
            run_time=TOTAL_TIME,
            rate_func=linear
        )