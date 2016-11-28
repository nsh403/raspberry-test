"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gpiozero import MCP3008
pot = MCP3008(0)

#    print pot.value


fig, ax = plt.subplots()

#x = np.arange(0, 2*np.pi, 0.5)        # x-array
x = np.linspace(0, 6.28, 100)        # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

y = x/10
cnt = len(y)
print cnt

def my_animate(i_caller):
    #print i_caller,
    
        
    for i in range(cnt):
        #y[i] = i/100. - i_caller/20.
        y[i] = pot.value
        
    line.set_ydata(y)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, my_animate, np.arange(1, 20), init_func=init,
    interval=50, blit=True)

plt.show()
