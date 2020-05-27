import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure(figsize=plt.figaspect(0.2))
ax = fig.add_subplot(1,5,1, projection = '3d')
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax = fig.add_subplot(1,5,2, projection = '3d')
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.summer,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax = fig.add_subplot(1,5,3, projection = '3d')
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.Pastel2,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )


ax = fig.add_subplot(1,5,4, projection = '3d')
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.gist_rainbow,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )

ax = fig.add_subplot(1,5,5, projection = '3d')
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.prism,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )


plt.show()