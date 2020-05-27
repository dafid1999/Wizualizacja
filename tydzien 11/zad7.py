from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

np.random.seed( 19680804 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot( projection = '3d' )

n = 20

for c, m, zlow, zhigh in [( 'r' , 'o' , - 5 ,  2 )]:
    ys = randrange(n, 0 , 100 )
    xs = randrange(n, 0 , 100 )
    ax.scatter(xs,ys,zs=0, c=c, marker=m)
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )


n=5
xs = randrange( n , 0, 100 )
ys = randrange( n , 0, 100 )

ax.plot(xs, ys, zs=0, c='g')
ax.set_zlim(0 , 1 )
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )

plt.show()