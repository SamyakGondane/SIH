import numpy as np
import matplotlib.pyplot as plt


#get input
rng = np.random.default_rng()



import manim
from manim import *


class beacon_generator (Scene) :

    def sqr_path (self, beacon) :

        len = rng.uniform(1, 5)
        speed = rng.uniform(1, 3)

        path = Square (side_length=len)
        left = rng.uniform(-1.5, 1.5)
        up = rng.uniform(-1.5, 1.5)
        path.shift(LEFT * left, UP * up)

        beacon.move_to(path.get_corner(UR))
        for _ in range(5) :
            self.play (MoveAlongPath(beacon, path), run_time=speed, rate_func=linear)
            #self.wait()

    def crcle_path (self, beacon) :

        r = rng.uniform(1, 5)
        speed = rng.uniform(1, 3)

        path = Circle(radius=r)
        left = rng.uniform(-1.5, 1.5)
        up = rng.uniform(-1.5, 1.5)
        path.shift(LEFT * left, UP * up)

        beacon.move_to(path.get_corner(UL))
        for _ in range(5) :
            self.play(MoveAlongPath(beacon, path), run_time=speed, rate_func=linear)

    def eight_path (self, beacon) :

        a = rng.uniform(1, 5)
        b = rng.uniform(1, 5)
        speed = rng.uniform(1, 3)

        path = ParametricFunction(
            lambda t: np.array([
                3 * np.sin(t),
                4 * np.sin(t) * np.cos(t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE
        )
        left = rng.uniform(-1.5, 1.5)
        up = rng.uniform(-1.5, 1.5)
        path.shift(LEFT * left, UP * up)

        beacon.move_to(path.get_corner(UL))
        for _ in range(5) :
            self.play(MoveAlongPath(beacon, path), run_time=speed, rate_func=linear)

    #add random path here



    def construct (self) :

        # Outer glow
        glow4 = Circle(radius=0.4, stroke_width=0, fill_color=GOLD, fill_opacity=0.05)
        glow3 = Circle(radius=0.3, stroke_width=0, fill_color=ORANGE, fill_opacity=0.08)
        glow2 = Circle(radius=0.25, stroke_width=0, fill_color=GOLD, fill_opacity=0.15)
        glow1 = Circle( radius=0.2, stroke_width=0, fill_color=YELLOW, fill_opacity=0.3)

        # Bright center
        beacon_dot = Dot(radius=0.1, color=WHITE)

        # Golden inner dot
        golden_core = Dot(radius=0.05, color=YELLOW)

        # Put large glows first so they stay behind
        beacon = VGroup(glow4, glow3, glow2, glow1, beacon_dot, golden_core)


        #DEFINE THE SPEED
        speed = 2

        #self.play(FadeIn(beacon, scale=0.5))

        get_path = rng.integers(low=0, high=3)

        if (get_path == 0) :
            self.sqr_path(beacon)
        elif (get_path == 1) :
            self.crcle_path(beacon)
        elif (get_path == 2) :
            self.eight_path(beacon)
