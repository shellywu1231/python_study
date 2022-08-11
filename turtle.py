
'''
import random
for i in range(15):
    value=random.randint(1,6)
    if value==6:
        continue
    print(value)

print("3個隨機樹分別{0},{0},{0}".format(random.randint(1,10)))

print("{}今天獲得{}比賽的第一名".format("小名","木工"))

name="shelly"
name="sam"
score=100
print("%s 成績為 %d" %(name,score))
print("{:8s}對於這次成績{}非常滿意".format(name,score))
'''
'''
for n in range(1,10):
     print("*"*n)
'''

import turtle as tu

#畫布設定
screen = tu.Screen()

screen.setup(500,500)

'''
#畫筆設定
tu.pensize(5)
tu.color('blue')

#畫筆(烏龜)動作
for i in range (4):
    # TODO: write code...
    tu.forward(120)
    tu.left(90)

#畫布結束設定    
tu.done()
'''
tu.showturtle()
tu.color('red')
tu.speed(0)
tu.begin_fill()
tu.left(90)
for i in range(200):
    tu.right(1)
    tu.forward(1)
    
tu.goto(0,-130)
tu.goto(-110.96,-20.57)
tu.penup()
tu.goto(0,0)
tu.pendown()
tu.home()
tu.left(90)
for i in range(200):
    tu.left(1)
    tu.forward(1)
    
tu.end_fill()

screen.bgcolor("#977C00")
tu.done()
