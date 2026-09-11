from manim import *

def create_beacon():

    glow4 = Circle(
        radius=0.4,
        stroke_width=0,
        fill_color=GOLD,
        fill_opacity=0.05
    )

    glow3 = Circle(
        radius=0.3,
        stroke_width=0,
        fill_color=ORANGE,
        fill_opacity=0.08
    )

    glow2 = Circle(
        radius=0.25,
        stroke_width=0,
        fill_color=GOLD,
        fill_opacity=0.15
    )

    glow1 = Circle(
        radius=0.2,
        stroke_width=0,
        fill_color=YELLOW,
        fill_opacity=0.3
    )

    beacon_dot = Dot(radius=0.1, color=WHITE)
    golden_core = Dot(radius=0.05, color=YELLOW)

    beacon = VGroup(
        glow4,
        glow3,
        glow2,
        glow1,
        beacon_dot,
        golden_core
    )

    return beacon