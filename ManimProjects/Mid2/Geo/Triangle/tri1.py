from manim import *


class Etude3(Scene):
    def construct(self):
        points = [
            (-2.5, -3, 0),
            (2.5, -3, 0),
            (0, 2, 0)
        ]

        text = Text("Triangle")
        text.to_edge(UP)
        text.font_size=65

        triangle = Polygon(*points, color=BLUE)

        self.add(text)
        self.add(triangle)
        self.wait()

        label_A = Text("A").scale(0.7).next_to(points[2], UP)
        label_B = Text("B").scale(0.7).next_to(points[0], LEFT)
        label_C = Text("C").scale(0.7).next_to(points[1], RIGHT)

        self.play(
            Write(label_A)
        )
        self.play(
            Write(label_B)
        )
        self.play(
            Write(label_C)
        )
        
