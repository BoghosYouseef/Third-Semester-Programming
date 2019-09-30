#import pygame as pg
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as colors

#pg.init()
#screen = pg.display.set_mode((1000, 1000))

#while True:
  #  for event in pg.event.get():
     #   if event.type == pg.QUIT:
     #       break

 #   pg.draw.rect(screen, (255, 255, 255), pg.Rect(30, 60, 90, 1))
  #  pg.display.flip()
x = np.random.rand(500) > 0.7
barprops = dict(aspect='auto', cmap='binary', interpolation='nearest')
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.09, 0.1, 0.8])
#ax1.set_axis_off()
ax1.imshow(x.reshape((-1, 1)), **barprops)
#plt.show()

help(fig.add_axes())
















