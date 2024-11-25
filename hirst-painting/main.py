# import colorgram
#
# colour_extract = colorgram.extract('image.jpg', 20)
# colour_list = []
#
# for i in range(len(colour_extract)):
#     colour = colour_extract[i]
#     rgb = colour.rgb
#     colour_tuple = (rgb.r, rgb.g, rgb.b)
#     colour_list.append(colour_tuple)
#
# (229, 228, 226), (225, 223, 224) backgrounds
# print(colour_list)

import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
tim.speed("fastest")

colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

t.hideturtle()

# def paint(dot_count):
#     for i in range(dot_count):
#         tim.dot(20, random.choice(colour_list))
#         tim.penup()
#         tim.fd(50)
#         tim.pendown()
lines = 0
num = 0
while lines < 10:
    for dot in range(10):
        tim.dot(20, random.choice(colour_list))
        tim.penup()
        tim.fd(50)
        tim.pendown()
    lines += 1
    num += 50
    tim.teleport(0, num)

    # tim_pos[1] += 50
    # tim.teleport(x=0, y=tim_pos[1])

screen.exitonclick()

