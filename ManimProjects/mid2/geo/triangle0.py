from manim import *

class Etude3(Scene):
    def construct(self):
        # 꼭짓점 정의하기
        points = [
            (-2.5, -3, 0) ,
            (2.5, -3, 0),
            (0, 2, 0)
        ]

        # 텍스트 추가
        text = Text("Triangle")
        text.to_edge(UP)
        text.font_size=72

        # Polygon 이용해서 이등변삼각형 만들기
        triangle = Polygon(*points, color=BLUE)

        # 화면에 텍스트와 삼각형을 각각 추가
        self.play(Write(text))  # 텍스트 애니메이션
     

        # 텍스트가 삼각형으로 변형되도록 하기 (텍스트 -> 삼각형)
        self.play(Transform(text[0], triangle), run_time=3)

        # 잠시 대기
        self.wait()
