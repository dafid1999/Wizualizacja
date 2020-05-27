import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680801 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot( 121 , projection = '3d' )
n = 20

for c, m, zlow, zhigh in [( 'r' , 'o' , - 50 , - 25 )]:
    xs = randrange(n, 0 , 100 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, 0 , 100 )
    ax1.scatter(xs,ys,zs, c =c, marker =m)

ax1.set_xlabel( 'X Label' )
ax1.set_ylabel( 'Y Label' )
ax1.set_zlabel( 'Z Label' )

ax2 = fig.add_subplot( 122 , projection = '3d' )
n=5
zs = randrange( n , 0, 100 )
xs = randrange( n , 0, 100 )
ys = randrange( n , 0, 100 )

ax2.plot(xs, ys, zs, c='g')

ax2.set_xlabel( 'X Label' )
ax2.set_ylabel( 'Y Label' )
ax2.set_zlabel( 'Z Label' )
plt.show()
