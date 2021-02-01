from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib import animation, rc
from IPython.display import HTML


class Hypocycloid:

    def __init__(self, ratio = 5.25, frames = 40, ncycles = 3):
        self.frames = frames
        self.ncycles = ncycles
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')

        ##big circle:
        theta = np.linspace(0,2*np.pi,40)
        x = np.cos(theta)
        y = np.sin(theta)

        self.big_circle, = self.ax.plot(x,y,'b-')

        ##small circle:
        self.small_r = 1./ratio
        r = self.small_r
        x = r*np.cos(theta)+1-r
        y = r*np.sin(theta)
        self.small_circle, = self.ax.plot(x,y,'k-')

        ##line and dot:
        self.line, = self.ax.plot([1-r,1],[0,0],'k-')
        self.dot, = self.ax.plot([1-r],[0], 'ko', ms=5)
        ##hypocycloid:
        self.hypocycloid, = self.ax.plot([],[],'r-')


        self.animation = FuncAnimation(
            self.fig, self.animate,
            frames=self.frames*self.ncycles,
            interval=50, blit=False,
            repeat_delay=2000,
        )


    def update_small_circle(self, phi):
        theta = np.linspace(0,2*np.pi,40)
        x = self.small_r*np.cos(theta)+(1-self.small_r)*np.cos(phi)
        y = self.small_r*np.sin(theta)+(1-self.small_r)*np.sin(phi)
        self.small_circle.set_data(x,y)


    def update_hypocycloid(self, phis):
        r = self.small_r
        x = (1-r)*np.cos(phis)+r*np.cos((1-r)/r*phis)
        y = (1-r)*np.sin(phis)-r*np.sin((1-r)/r*phis)
        self.hypocycloid.set_data(x,y)

        center = [(1-r)*np.cos(phis[-1]), (1-r)*np.sin(phis[-1])]

        self.line.set_data([center[0],x[-1]],[center[1],y[-1]])
        self.dot.set_data([center[0]], [center[1]])

    def animate(self, frame):
        frame = frame+1
        phi = 2*np.pi*frame/self.frames
        self.update_small_circle(phi)
        self.update_hypocycloid(np.linspace(0,phi,frame))

hypo = Hypocycloid(ratio=5.25, frames = 40, ncycles=3)

##un-comment the next line, if you want to save the animation as gif:
anim=hypo.animation.save('sdfhypocycloid.gif', writer='Pillow', fps=10, dpi=75)#
# HTML(anim.to_html5_video())
#plt.show()
