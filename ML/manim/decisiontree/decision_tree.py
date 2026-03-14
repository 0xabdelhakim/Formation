from manim import *

class DecisionTree(Scene):
    def construct(self):
        # Define the nodes
        root = Text("Root", font_size=36)
        left_child = Text("Left Child", font_size=36)
        right_child = Text("Right Child", font_size=36)

        # Position the nodes
        root.to_edge(UP)
        left_child.next_to(root, LEFT, buff=2)
        right_child.next_to(root, RIGHT, buff=2)

        # Create edges
        left_edge = Line(root.get_bottom(), left_child.get_top(), color=WHITE)
        right_edge = Line(root.get_bottom(), right_child.get_top(), color=WHITE)

        # Add nodes and edges to the scene
        self.add(root, left_child, right_child, left_edge, right_edge)
