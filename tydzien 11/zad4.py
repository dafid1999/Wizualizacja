import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

kolor = ['red','green','blue','yellow','cyan','orange','brown','indigo']
loskolor=[kolor[x] for y in range(4) for x in range(0+y,5+y,1)]

fig = plt.figure( figsize =(20 , 20 ))
ax1 = fig.add_subplot( 111 , projection = '3d' )

_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = (x + y)**1/2
bottom = np.zeros_like(top)
width = 0.8
depth = 0.7
ax1.bar3d(x, y, bottom, width, depth, top, color=loskolor, shade = True, lightsource=None )
ax1.set_title('Wykres kolorowy')

plt.show()