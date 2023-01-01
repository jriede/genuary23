rom anorganicorg import anorganicorg as ano
import numpy as np
import math
import string
import colorsys
from numpy.random import default_rng

#####################################
SX = 1000
SY = SX
ONE = 1./SX

XMAX = 1
YMAX = 1
dx = XMAX/5
dy = dx

filename = 'aoj-06-dists'
back = 1 # background color
front = 0 # foreground color

rng = default_rng()
vals = rng.pareto(10,31)
print(vals)

ao = ano.aolib(SX, SY, back, front)
ao.stroke_width(ONE)

ao.color(front, front, front, 1)
ao.ctx.save()

print(XMAX, dx)

#for j in range(0,int(YMAX/dy)+1):
for i in range(0,int(XMAX/dx)+1):
        print (i,int(XMAX/dx)+1)
        ao.ctx.identity_matrix()
        ao.ctx.scale(SX, SY)
        ao.ctx.translate(i*dx, YMAX/2)

        ao.circle(0, 0, XMAX*vals[i])
        ao.circle(0, 0, XMAX*vals[i+int(XMAX/dx)+1])
        ao.circle(0, 0, XMAX*vals[i+2*int(XMAX/dx)+1])
        ao.ctx.stroke()

        ao.write('img/{:s}-{:s}.png'.format(filename, str(i)))
