import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate a set of paths 
class PathGenerator():
    def __init__(self, time, speed):
        self.time = time
        self.speed = speed
        self.x = 0
        self.y = 0
    def printPos(self):
        print self.x
        print self.y
        print "--------------"
    def circlePath(self,time):
        self.x = np.cos(time)
        self.y = np.sin(time)
        self.time = time
    def infinityPath(self,time):
        self.x = np.cos(time)/(np.power(np.sin(time),2)+1)
        self.y = np.cos(time)*np.sin(time)/(np.power(np.sin(time),2)+1)
        self.time = time
    def squarePath(self,time):
        self.x = np.cos(time)/np.maximum(np.abs(np.sin(time)),np.abs(np.cos(time)))
        self.y = np.sin(time)/np.maximum(np.abs(np.sin(time)),np.abs(np.cos(time)))
        self.time = time
        
    def plotPath(self,x,y):
        
        def update_line(num, data, line):
            line.set_data(data[...,:num])
            return line,
        
        fig1 = plt.figure()
        
        data = np.array((x,y))
        l, = plt.plot([], [], 'r-')
        plt.xlim(-1.5, 1.5)
        plt.ylim(-1.5, 1.5)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('position')
        plt.grid()
        line_ani = animation.FuncAnimation(fig1, update_line, len(data[0]), fargs=(data, l),
            interval=200, blit=True)
        
        plt.show()


def main():
    path = PathGenerator(0,1)
    xvals = []
    yvals = []
    for t in np.arange(0,3.142*2,0.1):
        path.squarePath(t)
        xvals.append(path.x)
        yvals.append(path.y)
    path.plotPath(xvals,yvals)
    

        




if __name__ == "__main__":
    main()