import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
sin = np.sin(x)+2
cos = np.sin(-x)
fig, ax = plt.subplots()
line1,=ax.plot(x, sin, label='sin(x)')
line2,=ax.plot(x, cos, label='sin(x)')

ax.annotate('local max', xy=(7.8, 3), xytext=(9.5, 3.1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title("Wykres sin(x), sin(x)")

plt.legend(loc=6)
plt.show()

fig, ax=plt.subplots()
x= range(1,21)
y= [1/y for y in x]
line,=ax.plot(x,y, label='f(x)=1/x')
plt.title('Wykres f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0,21,1))
plt.yticks(np.arange(0,1.1,0.1))
ax.annotate('f(15)=0.06', xy=(15, 0.06), xytext=(17,0.8),
            arrowprops=dict(facecolor='black', shrink=0.01))
            
plt.legend()

plt.show()