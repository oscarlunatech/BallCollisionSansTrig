
# I confirm that I did not use codes from anyone else and that the work I submit is my own and my own only.

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import numpy as np


t = 0
t_final = 50
dt = 0.02
alpha = 0.8
beta = 0.98
r = 0.05

def stepInc(ball):
    ball.x = ball.x + dt * ball.u
    ball.y = ball.y + dt * ball.v
def wallCollisionCheck(ball):
    # if hits right wall
    if (ball.x + r > 1):
        ball.x = ball.x - dt * ball.u
        dtnew = abs((1 - 0.05 - ball.x)/ball.u)
        ball.x = ball.x + dtnew * ball.u
        ball.u *= -1 * alpha
        ball.v *= beta
        ball.x = ball.x + (dt - dtnew) * ball.u
    # if hits left wall
    if (ball.x - r < 0):
        ball.x = ball.x - dt * ball.u
        dtnew = abs((ball.x - 0.05)/ball.u)
        ball.x = ball.x + dtnew * ball.u
        ball.u *= -1 * alpha
        ball.v*= beta
        ball.x = ball.x + (dt - dtnew) * ball.u

    # if hits top wall
    if (ball.y + r > 1):
        ball.y = ball.y - dt * ball.v
        dtnew = abs((1 - 0.05 - ball.y)/ball.v)
        ball.y = ball.y + dtnew * ball.v
        ball.v *= -1 * alpha
        ball.u*= beta
        ball.y = ball.y + (dt - dtnew) * ball.v

    # if hits bottom wall
    if (ball.y - r < 0):
        ball.y = ball.y - dt * ball.v
        dtnew = abs((ball.y - 0.05)/ball.v)
        ball.y = ball.y + dtnew * ball.v
        ball.v *= -1 * alpha
        ball.u *= beta
        ball.y = ball.y + (dt - dtnew) * ball.v
def ballCollisionCheck(ball1,ball2):
    # if collision between blue and red
    if (math.sqrt((ball1.x-ball2.x)**2 + (ball1.y-ball2.y)**2) < (2*r)):
        # move back a step
        ball2.x = ball2.x - dt * ball2.u
        ball2.y = ball2.y - dt * ball2.v
        ball1.x = ball1.x - dt * ball1.u
        ball1.y = ball1.y - dt * ball1.v
        # make them touch
        dtnew = (math.sqrt((ball1.x-ball2.x)**2 + (ball1.y-ball2.y)**2) - (2*r))/math.sqrt((ball1.u-ball2.u)**2 + (ball1.v-ball2.v)**2)
        ball2.y = ball2.y + dtnew * ball2.v
        ball2.x = ball2.x + dtnew * ball2.u
        ball1.y = ball1.y + dtnew * ball1.v
        ball1.x = ball1.x + dtnew * ball1.u

        # normal projection stuff

        # create normal and tangent basis
        n1 = (ball2.x - ball1.x)/math.sqrt((ball2.x-ball1.x)**2 + (ball2.y-ball1.y)**2)
        n2 = (ball2.y - ball1.y)/math.sqrt((ball2.x-ball1.x)**2 + (ball2.y-ball1.y)**2)
        t1 = n2 * -1
        t2 = n1
        normal = np.array([n1,n2])
        tangent = np.array([t1,t2])

        #project onto n  t basis
        V2 = np.array([ball2.u,ball2.v])
        V1 = np.array([ball1.u,ball1.v])
        Projected_2 = np.array([np.dot(V2, normal),np.dot(V2,tangent)])
        Projected_1 = np.array([np.dot(V1, normal),np.dot(V1,tangent)])

        # swap normal components
        tempSwap = Projected_2[0]
        Projected_2[0] = Projected_1[0]
        Projected_1[0] = tempSwap

        # transition back V to i, j
        V2 = Projected_2[0] * normal + Projected_2[1] * tangent
        V1 = Projected_1[0] * normal + Projected_1[1] * tangent
        ball2.u = V2[0]
        ball2.v = V2[1]
        ball1.u = V1[0]
        ball1.v = V1[1]


        # finish step with new velocities
        ball2.y = ball2.y + (dt - dtnew) * ball2.v
        ball2.x = ball2.x + (dt - dtnew) * ball2.u
        ball1.y = ball1.y + (dt - dtnew) * ball1.v
        ball1.x = ball1.x + (dt - dtnew) * ball1.u
class Ball:
    def __init__(self, x, y, u, v):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.x_animation = []
        self.y_animation = []

    def append(self):
        self.x_animation.append(self.x)
        self.y_animation.append(self.y)

redBall = Ball(0.75, 5*r, -0.1, 0.5 )
blueBall = Ball(0.25,5.5*r, 0.11, 0.2)
yellowBall = Ball(0.15, 0.45, 0.21, -0.4)
purpleBall = Ball(0.1, 0.95, 1 , -0.4)
orangeBall = Ball(0.95, 0.5, -0.4 , 0)
blackBall = Ball(0.35, 0.95, 0 , -0.7)
whiteBall = Ball(0.95, 0.1, -.2 , 1)

#The creator
while t < t_final:

    stepInc(redBall)
    stepInc(blueBall)
    stepInc(yellowBall)
    stepInc(purpleBall)
    stepInc(orangeBall)
    stepInc(blackBall)
    stepInc(whiteBall)

    wallCollisionCheck(redBall)
    wallCollisionCheck(blueBall)
    wallCollisionCheck(yellowBall)
    wallCollisionCheck(purpleBall)
    wallCollisionCheck(orangeBall)
    wallCollisionCheck(blackBall)
    wallCollisionCheck(whiteBall)

    # could make this a nested for loop but I'd have to put the balls in a list and I'm tired
    ballCollisionCheck(redBall,blueBall)
    ballCollisionCheck(redBall,yellowBall)
    ballCollisionCheck(redBall,purpleBall)
    ballCollisionCheck(redBall,orangeBall)
    ballCollisionCheck(redBall,blackBall)
    ballCollisionCheck(redBall,whiteBall)
    ballCollisionCheck(blueBall,yellowBall)
    ballCollisionCheck(blueBall,purpleBall)
    ballCollisionCheck(blueBall,orangeBall)
    ballCollisionCheck(blueBall,blackBall)
    ballCollisionCheck(blueBall,whiteBall)
    ballCollisionCheck(yellowBall,purpleBall)
    ballCollisionCheck(yellowBall,orangeBall)
    ballCollisionCheck(yellowBall,blackBall)
    ballCollisionCheck(yellowBall,whiteBall)
    ballCollisionCheck(purpleBall,orangeBall)
    ballCollisionCheck(purpleBall,blackBall)
    ballCollisionCheck(purpleBall,whiteBall)
    ballCollisionCheck(orangeBall,blackBall)
    ballCollisionCheck(orangeBall,whiteBall)
    ballCollisionCheck(blackBall,whiteBall)





    redBall.append()
    blueBall.append()
    yellowBall.append()
    purpleBall.append()
    orangeBall.append()
    blackBall.append()
    whiteBall.append()
    t += dt



# function that draws each frame of the animation
def animate(i):
    ax.clear()
    circler = plt.Circle((redBall.x_animation[i], redBall.y_animation[i]), r, color="red")
    circleb = plt.Circle((blueBall.x_animation[i], blueBall.y_animation[i]), r, color="blue")
    circley = plt.Circle((yellowBall.x_animation[i], yellowBall.y_animation[i]), r, color="yellow")
    circlep = plt.Circle((purpleBall.x_animation[i], purpleBall.y_animation[i]), r, color="purple")
    circleo = plt.Circle((orangeBall.x_animation[i], orangeBall.y_animation[i]), r, color="orange")
    circlek = plt.Circle((blackBall.x_animation[i], blackBall.y_animation[i]), r, color="black")
    circlew = plt.Circle((whiteBall.x_animation[i], whiteBall.y_animation[i]), r, color="white")
    ax.add_artist(circler)
    ax.add_artist(circleb)
    ax.add_artist(circley)
    ax.add_artist(circlep)
    ax.add_artist(circleo)
    ax.add_artist(circlek)
    ax.add_artist(circlew)

# create the figure and axes objects
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_aspect(1)
ax.set_facecolor("forestgreen")

# run the animation
ani = FuncAnimation(fig, animate, frames=int(t_final/dt) ,interval=1000 * dt, repeat=False)

plt.show()
