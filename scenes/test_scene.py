from manim import *
import math
import operator
from sympy import *
from helper_functions.coordinates import cart2pol, pol2cart
import os
import random
import numpy as np 

class Fractions(Scene):
    #A few simple shapes
    def construct(self):
        speed = 0
        circle = Circle(color=WHITE,radius=2)
        angle1 = 3*math.pi/2
        angle2 = math.pi/2
        arc1 = Arc(radius=2,angle=angle1)
        arc1.move_to(UP*0.01)
        arc1.rotate(angle2)
        arc2 = Arc(radius=2,angle=angle2)
        arc2.move_to((0.99,1,0))
        line1=Line(np.array([0,2.01,0]),np.array([0,-0.01,0]))
        line2=Line(np.array([2,0,0]),np.array([-0.01,0,0]))
        line3=Line(np.array([0,2.01,0]),np.array([0,-0.01,0]))
        line4=Line(np.array([2,0,0]),np.array([-0.01,0,0]))
        segment = VGroup(line1,line2,arc2)
        main_segment = VGroup(line3,line4,arc1)
        animation_segment = ApplyMethod(segment.shift, (1,1,0))
        one_quarter=TextMobject("$\\frac{1}{4}$")
        one_quarter.move_to((UP+RIGHT)*1.8)
        three_quarter=TextMobject("$\\frac{3}{4}$")
        three_quarter.move_to((DOWN+LEFT)*0.7)
        three_square = VGroup(Line((0,2,0),(-2,2,0)),Line((-2,2,0),(-2,-2,0)),Line((-2,-2,0),(2,-2,0)),Line((2,-2,0),(2,0,0)))
        three_square.flip(axis=(UP+RIGHT))
        square = VGroup(Line((0,2,0),(2,2,0)),Line((2,2,0),(2,0,0)))
        square.move_to((UP+RIGHT)*2)
        square.flip(axis=(UP+RIGHT))

        self.play(ShowCreation(circle))
        self.add(arc1,arc2)
        self.wait(1*speed)
        self.play(ShowCreation(line1),ShowCreation(line2))
        self.add(line3,line4)
        self.remove(circle)
        self.wait(1*speed)
        self.play(animation_segment)
        self.wait(2*speed) 
        self.play(Indicate(segment))  
        self.play(Write(one_quarter))
        self.wait(1*speed)
        self.play(Indicate(main_segment))  
        self.play(Write(three_quarter))
        self.wait(2*speed)
        self.play(Transform(arc2,square))
        self.wait(1*speed)
        self.play(Transform(arc1,three_square))
        self.wait(2*speed)

    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class Animation1(Scene):
    #A few simple shapes
    def construct(self):
        speed = 0
        start = Dot()
        copy = start.copy()
        parts = 10
        angle = 360/parts
        rand_number_list = list(set([random.randint(1,i) for i in range(1,101)]))
        random.shuffle(rand_number_list)
        print(rand_number_list)
        red_points = [(math.cos(angle*i),math.sin(angle*i),0) for i in range(0,11)]
        blue_points = [(random.randint(0,10)*i/1000,0,0) for i in range(0,10)]

        red_coins = VGroup(*[copy.copy().move_to(point) for point in red_points])
        blue_coins = VGroup(*[copy.copy().move_to(point) for point in blue_points])
        self.play(ShowCreation(red_coins),ShowCreation(blue_coins))
        red_coins.set_color(RED)
        blue_coins.set_color(BLUE)
        self.play(FadeIn(red_coins),FadeIn(blue_coins))
        self.play(ApplyMethod(red_coins.shift,(0,1,0)))
        self.play(ApplyMethod(blue_coins.shift,(0,-1,0)))
        self.play(ApplyMethod(red_coins[0].move_to,(0,2,0)))
        for i in range(1,len(red_coins)):
            self.play(ApplyMethod(red_coins[i].move_to,(red_coins[0].get_center() + (random.randint(-10,10)/10,random.randint(-10,10)/10,0)),run_time=0.4))
        self.play(ApplyMethod(blue_coins[0].move_to,(0,-2,0)))
        for i in range(1,len(blue_coins)):
            self.play(ApplyMethod(blue_coins[i].move_to,(blue_coins[0].get_center() + (random.randint(-10,10)/10,random.randint(-10,10)/10,0)),run_time=0.4))
        self.wait(1)

class Animation2(Scene):
    #A few simple shapes
    def construct(self):
        piles = 5
        start = Dot()
        copy = start.copy()
        text = TextMobject("$\\frac{1}{" + str(piles) + "}$")
        grid = []
        for i in range(0,10):
            for j in range(0,10):
                grid.append((i/5,j/5,0))
        coins = VGroup(*[copy.copy().move_to(point) for point in grid])
        coins.shift((-1,-1,0))

        self.wait(1)
        self.play(FadeIn(coins))
        self.wait(1)
        fraction_points = []
        for p in range(0,piles):
            for i in range(int(p*100/piles),int((p+1)*100/piles)):
                side = int(math.ceil(math.sqrt(100/piles)))
                square = []
                for j in range(0,side):
                    for k in range(0,side):
                        square.append(tuple(map(operator.add,(j/5,k/5,0),(-5 + (12/piles)*p ,2,0))))
                self.play(ApplyMethod(coins[i].move_to,square[i%int(100/piles)]),run_time = 0.3)
            fraction_points.append(coins[int(p*100/piles)].get_center())
        fractions = VGroup(*[text.copy().move_to(tuple(map(operator.add,point,(1/p,-1,0)))) for point in fraction_points])
        self.play(FadeIn(fractions))
        self.wait(1)



class RoundCake(Scene):
    def construct(self):
        print("How many pieces do you want to cut your cake into?")
        pieces = int(input())
        pieces_angle = 2*np.pi/pieces
        circle = Circle(radius = 2, color = WHITE)
        initial_line = Line(np.array([0,0,0]),np.array([2,0,0]))
        initial_line1 = initial_line.copy().rotate(angle = pieces_angle, about_point = np.array([0,0,0]))
        just_lines = Line(np.array([0,0,0]),np.array([pol2cart(2,pieces_angle)[0],pol2cart(2,pieces_angle)[1],0]))
        piece = VGroup(Arc(start_angle = 0, angle = pieces_angle ,radius = 2),Line(np.array([0,0,0]),np.array([2,0,0])),Line(np.array([0,0,0]),np.array([pol2cart(2,pieces_angle)[0],pol2cart(2,pieces_angle)[1],0])))
        dashed_piece = VGroup(Arc(start_angle = 0, angle = pieces_angle ,radius = 2),DashedVMobject(Line(np.array([0,0,0]),np.array([2,0,0]))),DashedVMobject(Line(np.array([0,0,0]),np.array([pol2cart(2,pieces_angle)[0],pol2cart(2,pieces_angle)[1],0]))))
        fraction = TextMobject(r"$\frac{1}{" + str(pieces) + r"}$")

        piece_list = []
        for i in range(0,int(pieces)):
            piece_copy = dashed_piece.copy().rotate(angle = i * pieces_angle, about_point = np.array([0,0,0]))
            piece_list.append(piece_copy.copy())
        dashed_pieces = VGroup(*piece_list)

        piece_list = []
        for i in range(0,int(pieces)):
            piece_copy = piece.copy().rotate(angle = i * pieces_angle, about_point = np.array([0,0,0]))
            piece_list.append(piece_copy.copy())
        pieces = VGroup(*piece_list)

        self.play(ShowCreation(circle),run_time = 2)
        self.play(ShowCreation(dashed_pieces), run_time = 2)
        self.remove(circle)
        self.wait(2)

        fraction_list = []
        self.play(ShowCreation(initial_line))
        self.play(ShowCreation(initial_line1))
        for p in range(0,len(dashed_pieces)):
            if p > 0: self.remove(lines_copy)
            self.remove(dashed_pieces[p])
            self.add(pieces[p])
            if p == (len(dashed_pieces)-1): self.remove(initial_line)
            fraction_copy = fraction.copy().shift([pol2cart(2.3, pieces_angle*(p+0.5))[0],pol2cart(2.3, pieces_angle*(p+0.5))[1],0])
            fraction_list.append(fraction_copy)
            self.play(ApplyMethod(pieces[p].shift,[pol2cart(1, pieces_angle*(p+0.5))[0],pol2cart(1, pieces_angle*(p+0.5))[1],0]))
            lines_copy = just_lines.copy().rotate(angle = p * pieces_angle, about_point = np.array([0,0,0]))
            if p != (len(dashed_pieces)-1): self.add(lines_copy)
            if p > 0: self.remove(lines_copy1)
            lines_copy1 = lines_copy.copy().rotate(angle = pieces_angle, about_point = np.array([0,0,0]))
            if p != (len(dashed_pieces)-1): self.play(ShowCreation(lines_copy1))
            if p == 0: self.remove(initial_line1)
            if p == (len(dashed_pieces)-2): self.remove(lines_copy1)
            
        self.wait(2)
        fractions = VGroup(*fraction_list)
        self.play(Write(fractions))
        self.wait(2)

class Sweets(Scene):
    def construct(self):
        end = Polygon([0,0.2,0],[-1,0.5,0],[-1,0.5,0],[-1,-0.5,0],[-1,-0.5,0],[0,-0.2,0])
        end.set_fill(WHITE, opacity = 1)
        end_copy = end.copy().rotate(angle = np.pi).shift([1.9,0,0])
        centre = Ellipse(width=2, height=1)
        end.shift([-0.9,0,0])
        sweet = VGroup(end, end_copy, centre)
        sweet.set_color(WHITE)
        sweet[2].set_fill(RED, opacity=1)
        sweet.scale(0.4)
        for i in range(0,12):
            self.play(FadeIn(sweet.copy().shift([0,i/2,0])))

        self.play(ShowCreation(sweet), run_time = 3)



class Card(Scene):
    def construct(self):
        start = Dot()
        copy = start.copy()
        birthday1 = TextMobject(r"Happy Birthday")
        birthday1.scale(2)
        birthday2 = TextMobject(r"$\mathcal{H}{\alpha}{\rho}{\rho}{\gamma}  ~ \mathcal{B}\iota rt{\hbar}{\delta}{\alpha}{\gamma}$")
        birthday2.scale(2)
        dad = TextMobject(r"Dad")
        from_ = TextMobject(r"From Jamie")
        from__ = TextMobject(r"(Your favourite son)")
        from_.shift([0,-1,0])
        from__.shift([0,-1,0])
        SVG_IMAGE_DIR = r"C:\Users\James\Git\Repos\Manim\manim\media\design\svg_images\\"
        svg = SVGMobject("cake.svg")
        svg.shift(RIGHT*4 + DOWN *2)

        self.play(Write(birthday1), ShowCreation(svg), run_time = 5)
        self.wait(2)
        self.play(Transform(birthday1,birthday2), run_time = 2)
        self.wait(2)
        self.play(ApplyMethod(birthday1.shift,2*UP))
        self.wait(2)
        self.play(Write(dad), run_time = 2)
        self.wait(2)
        self.play(Write(from_), run_time = 2)
        self.wait(3)
        self.play(Transform(from_,from__), run_time = 2)
        

class Diff(GraphScene):
    CONFIG = {
        "y_min" : 0,
        "y_axis_height": 10,
        "x_max" : 10,
        "x_min" : 0,
        "x_axis_width": 10,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLACK,
        "x_axis_label": "",
        "y_axis_label": "",
        "function_color": WHITE,
        "graph_origin": 5 * DOWN + 5 * LEFT,
    }

    def func_to_general_graph(self, x):
        return((-(x-7)**(2)+49)/(7))
    
    def tang(self, x, x0):
        return((-(2/7)*x0 +2)*x + ((-(x0-7)**(2)+49)/(7)) - (-(2/7)*x0 +2)*x0)
    
    def func_diff(self, x):
        return((8/7)*x + 9/7)


    def construct(self):
        #Make graph
        self.setup_axes(animate=True)

        general_graph = self.get_graph(self.func_to_general_graph,self.function_color, x_min=1, x_max=10)
        general_graph_lab = self.get_graph_label(general_graph, label = "y = f(x)").scale(0.75).shift(RIGHT*0.2)


        point_p = Dot(self.coords_to_point(3,self.func_to_general_graph(3)))
        point_p_lab = TextMobject(r"$\mathrm{P}(x,\phantom{y})$").move_to(point_p.get_center() + LEFT*1.75).scale(0.75)
        just_y = TextMobject(r"$y)$").scale(0.75).align_to(point_p_lab,RIGHT).align_to(point_p_lab,UP)
        point_p_lab1 = TextMobject(r"$\mathrm{P}(x,\phantom{f(x)})$").scale(0.75).align_to(point_p_lab,LEFT).align_to(point_p_lab,UP)

        circle = Circle(radius = np.sqrt(4**(2)+ ((33)/(7)-(17)/(14))**2)).move_to(self.coords_to_point(7,17/14))
        centre = Dot(self.coords_to_point(7,17/14))
        circle_group = VGroup(circle, centre)
        radius = Line(point_p.get_center(), self.coords_to_point(7,17/14))
        print(self.point_to_coords([0,0,0]))

        point_q = Dot(self.coords_to_point(6,self.func_to_general_graph(6)))
        point_q_lab = TextMobject(r"$\mathrm{Q}(x + \delta x,f(x + \delta x))$").scale(0.75).align_to(point_p_lab, LEFT).align_to(point_q, BOTTOM)
        invis_q = Dot(self.coords_to_point(6,100))

        f_of_x = TextMobject(r"$f(x)$").move_to(general_graph_lab.get_right()).scale(0.75)
        f_of_x.align_to(general_graph_lab,RIGHT).align_to(general_graph_lab,UP)

        p_q_line = Line(point_p.get_center(),point_q.get_center()).set_color(BLUE)
        p_q_tri = Polygon(point_p.get_center(),point_q.get_center(),self.coords_to_point(6,self.func_to_general_graph(3)))

        p_q_tri_adj1 = TextMobject(r"$x + \delta x - x$").scale(0.75).set_color(BLUE)
        p_q_tri_adj = TextMobject(r"$\delta x$").scale(0.75).set_color(BLUE)
        p_q_tri_adj1.move_to(p_q_tri.get_bottom()).shift(p_q_tri_adj1.get_top() - p_q_tri.get_bottom() + DOWN*0.4)
        p_q_tri_adj.move_to(p_q_tri.get_bottom()).shift(p_q_tri_adj.get_top() - p_q_tri.get_bottom() + DOWN*0.4)

        p_q_tri_opp = TextMobject(r"$f(x + \delta x) - f(x)$").scale(0.75).set_color(BLUE)
        p_q_tri_opp.move_to(p_q_tri.get_right()).shift(p_q_tri.get_right() - p_q_tri_opp.get_left() + RIGHT*0.2)

        group = VGroup(p_q_tri,p_q_tri_opp,p_q_tri_adj1, point_q, point_q_lab)
        p_lab_group = VGroup(point_p_lab, f_of_x)

        def update_triangle(group):
            triangle, lab1, lab2, point, point_lab = group
            new_point = Dot(self.coords_to_point(self.point_to_coords(invis_q.get_center())[0],self.func_to_general_graph(self.point_to_coords(invis_q.get_center())[0])))
            point.become(new_point)
            new_triangle=Polygon(point_p.get_center(),point_q.get_center(),self.coords_to_point(self.point_to_coords(point_q.get_center())[0],self.func_to_general_graph(3)))
            lab1.move_to(triangle.get_right()).shift(triangle.get_right() - lab1.get_left() + RIGHT*0.2)
            lab2.move_to(triangle.get_bottom()).shift(lab2.get_top() - triangle.get_bottom() + DOWN*0.4)
            point_lab.align_to(point_p_lab, LEFT).align_to(point, BOTTOM)
            triangle.become(new_triangle)
        
        #Display graph
        self.play(ShowCreation(general_graph))
        self.play(Write(general_graph_lab))
        self.wait(1)

        #Draw in the tangents
        points_list = []
        tangents_list = []
        for i in range(1,11):
            def tangent_func(x):
                return(self.tang(x, i))
            points_list.append(Dot(self.coords_to_point(i,self.func_to_general_graph(i))))
            tangents_list.append(self.get_graph(tangent_func,color = RED, x_min=1, x_max=10))
            points = VGroup(*points_list)
            tangents = VGroup(*tangents_list)
        for point in points: self.play(ShowCreation(point))
        for tangent in tangents: self.play(ShowCreation(tangent))
        self.wait(1)
        self.remove(general_graph)
        self.wait(1)
        self.play(ShowCreation(general_graph))
        self.play(FadeOut(points), FadeOut(tangents))
        self.wait(1)

        #Add point p and its tangent
        self.add(point_p)
        self.play(Write(point_p_lab), Write(just_y))
        self.wait(1)
        self.play(ShowCreation(tangents[2]))
        self.wait(1)

        #Add and remove circle
        self.play(ShowCreation(circle_group))
        self.wait(1)
        self.play(ShowCreationThenFadeOut(radius))
        self.play(FadeOut(circle_group))

        #Change y to f(x)
        self.play(Indicate(just_y))
        self.play(FadeOut(just_y))
        self.play(Transform(point_p_lab, point_p_lab1))
        self.play(Indicate(general_graph_lab))
        self.add(f_of_x)
        self.play(
            ApplyMethod(f_of_x.move_to, point_p_lab.get_right() + LEFT*0.45),
            run_time = 3
            )
        self.wait(1)
        self.play(Transform(point_p_lab, point_p_lab1))
        self.wait(1)

        #Add point q
        self.add(point_q)
        self.play(Write(point_q_lab))
        self.wait(1)

        #Draw triangle
        self.play(ShowCreation(p_q_line))
        self.play(ShowCreation(p_q_tri))
        self.remove(p_q_line)
        self.play(Write(p_q_tri_adj1))
        self.play(Write(p_q_tri_opp))
        self.wait(1)

        #Move point q towards point p
        self.play(Transform(p_q_tri_adj1,p_q_tri_adj))
        self.play(
            ScaleInPlace(point_q_lab,0.75),
            ScaleInPlace(p_lab_group,0.75),
            ScaleInPlace(p_q_tri_opp,0.75),
            ScaleInPlace(p_q_tri_adj1,0.75),
            UpdateFromFunc(group, update_triangle),
            ApplyMethod(invis_q.shift, LEFT*2),
            run_time = 3,
            )
        self.wait(1)
        




#---------------------------------------
class PlotFunctions(GraphScene):
    CONFIG = {
    "x_min" : -10,
    "x_max" : 10,
    "y_min" : -10,
    "y_max" : 10,
    "x_tick_frequency": 2,
    "y_tick_frequency": 2,
    "y_axis_height": 5,
    "x_axis_width": 5,
    "graph_origin": ORIGIN,
    "always_update_mobjects": True,
    "always_continually_update": True,
}  
    def construct(self):      
        self.setup_axes(animate=False)
       
        Origin=self.coords_to_point(0,0)  
        Point1=Dot(color=RED)
        line=DashedLine(Origin,Point1)
       
        def update_line(line):
            new_line=DashedLine(Origin,Point1)
            line.become(new_line)
       
        self.add(line)
        self.play(FadeIn(Point1))        
 
        self.play(
            UpdateFromFunc(line,update_line),
            Point1.to_edge, DOWN + LEFT,
            rate_func=there_and_back,
            run_time=5,        
        )    
        self.wait(3)
#---------------------------------------


NEW_BLUE = "#68a8e1"

class Thumbnail(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=False)
        def func(x):
            return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5

        def rect(x):
            return 2.775*(x-1.5)+3.862
        recta = self.get_graph(rect,x_min=-1,x_max=5)
        graph = self.get_graph(func,x_min=0.2,x_max=9)
        graph.set_color(NEW_BLUE)
        input_tracker_p1 = ValueTracker(1.5)
        input_tracker_p2 = ValueTracker(3.5)

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)
        # 
        input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0)
        input_triangle_p2 = input_triangle_p1.copy()
        output_triangle_p2 = output_triangle_p1.copy()

        for triangle in input_triangle_p1, output_triangle_p1,input_triangle_p2, output_triangle_p2:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        
        # 
        x_label_p1 = TexMobject("a")
        output_label_p1 = TexMobject("f(a)")
        x_label_p2 = TexMobject("b")
        output_label_p2 = TexMobject("f(b)")
        v_line_p1 = get_v_line(input_tracker_p1)
        v_line_p2 = get_v_line(input_tracker_p2)
        h_line_p1 = get_h_line(input_tracker_p1)
        h_line_p2 = get_h_line(input_tracker_p2)
        graph_dot_p1 = Dot(color=WHITE)
        graph_dot_p2 = Dot(color=WHITE)

        # reposition mobjects
        x_label_p1.next_to(v_line_p1, DOWN)
        x_label_p2.next_to(v_line_p2, DOWN)
        output_label_p1.next_to(h_line_p1, LEFT)
        output_label_p2.next_to(h_line_p2, LEFT)
        input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
        graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

        #updaters


        #
        self.play(
            ShowCreation(graph),
        )
        # Animacion del punto a
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            Write(x_label_p1),
            ShowCreation(v_line_p1),
            ShowCreation(h_line_p1),
            Write(output_label_p1),
            DrawBorderThenFill(output_triangle_p1),
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(v_line_p2),
            ShowCreation(h_line_p2),
            Write(output_label_p2),
            DrawBorderThenFill(output_triangle_p2),
            GrowFromCenter(graph_dot_p2),
            GrowFromCenter(graph_dot_p1),
            run_time=0.5
        )

        group = VGroup(
            input_triangle_p2,
            output_triangle_p2,
            x_label_p2,
            output_label_p2,
            v_line_p2,
            h_line_p2,
            graph_dot_p2,
            )

        def update_group(mob,alpha):
            it,ot,xl,yl,vl,hl,d = mob
            hl.become(get_h_line(input_tracker_p2)).fade(alpha)
            vl.become(get_v_line(input_tracker_p2)).fade(alpha)
            it.next_to(vl, DOWN, buff=0).fade(alpha)
            ot.next_to(hl, LEFT, buff=0).fade(alpha)
            xl.next_to(vl, DOWN).fade(alpha)
            yl.next_to(hl, LEFT).fade(alpha)
            d.move_to(get_graph_point(input_tracker_p2))

        ###################
        solpe_recta = self.get_secant_slope_group(
            1.9, recta, dx = 1.4,
            df_label = None,
            dx_label = None,
            dx_line_color = PURPLE,
            df_line_color= ORANGE,
            )
        grupo_sec = self.get_secant_slope_group(
            1.5, graph, dx = 2,
            df_label = None,
            dx_label = None,
            dx_line_color = "#942357",
            df_line_color= "#3f7d5c",
            secant_line_color = RED,
        )
        start_dx = grupo_sec.kwargs["dx"]
        start_x = grupo_sec.kwargs["x"]
        def update_slope(group, alpha):
            dx = interpolate(start_dx, 0.001, alpha)
            x = interpolate(start_x, 1.5, alpha)
            kwargs = dict(grupo_sec.kwargs)
            kwargs["dx"] = dx
            kwargs["x"] = x
            new_group = self.get_secant_slope_group(**kwargs)
            group.become(new_group)
            return group

        self.add(
            input_triangle_p2,
            graph_dot_p2,
            v_line_p2,
            h_line_p2,
            output_triangle_p2,
        )
        self.add_foreground_mobjects(grupo_sec)
        self.add_foreground_mobjects(graph_dot_p1,graph_dot_p2)
        self.play(FadeIn(grupo_sec))
        self.wait()

        self.play(
            input_tracker_p2.set_value,input_tracker_p1.get_value(),
            UpdateFromAlphaFunc(grupo_sec,update_slope),
            UpdateFromAlphaFunc(group,update_group),
            )

        kwargs = {
            "x_min" : 2,
            "x_max" : 8,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
        }
        self.graph=graph
        iteraciones=6


        self.rect_list = self.get_riemann_rectangles_list(
            graph, iteraciones,start_color=PURPLE,end_color=ORANGE, **kwargs
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x : 0), dx = 0.5,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs
        )
        rects = self.rect_list[0]
        self.transform_between_riemann_rects(
            flat_rects, rects, 
            replace_mobject_with_target_in_scene = True,
            run_time=0.9
        )

        for j in range(4,6):
            for w in self.rect_list[j]:
                    color=w.get_color()
                    w.set_stroke(color,1.5)
        for j in range(1,6):
            self.transform_between_riemann_rects(
            self.rect_list[j-1], self.rect_list[j], dx=1,
            replace_mobject_with_target_in_scene = True,
            run_time=0.9
            )