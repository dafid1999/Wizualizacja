import numpy as np
import matplotlib.pyplot as plt

x= range(1,21)
y= [1/y for y in x]
plt.plot(x,y,'g:>', label='f(x)=1/x')
plt.title('Wykres funkcji f(x) dla x [1,20]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,2.5))
plt.yticks(np.arange(0,1.1,0.2))
plt.legend()

plt.show()