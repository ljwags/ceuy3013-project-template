# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# -- Imports ------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# -- First class --------------------------------------------------------------
class HorizontalAlignment:

    sidefrictionfactor = 0.15
    superelevation = 0.10

    def __init__(self, xcor, ycor, speed, tanglen):
        self.xcor = xcor
        self.ycor = ycor
        self.speed = speed
        self.tanglen = tanglen

        if speed <= 0:
            raise ValueError('Invalid speed.')
        if tanglen <= 0:
            raise ValueError('Invalid tangent length.')

    def radius(self):
        """ This calculates the radius of the curve. This is R on the horizontal curve diagram in the README.md file.
        """
        if self.speed:
            return (self.speed**2)/(15*(0.01*self.superelevation+self.sidefrictionfactor))
    
    def intersectangle(self):
        """ This calculates the intersection of the angle of the two tangent lines and converts to degrees.
        This is I on the horizontal curve diagram.
        """
        if self.tanglen:
            return (2*np.arctan(self.tanglen/self.radius()))*(180/np.pi)

    def longchordlen(self):
        """ This calculates the length of the long cord from the point of curve to the point of tangent.
        This is not the length of the curve but the short distance between the beginning and end points.
        This is LC on the horizontal curve diagram.
        """
        if self.tanglen and self.intersectangle():
            return (2*self.tanglen*np.cos((self.intersectangle()*(np.pi/180))/2))

    def midordlen(self):
        """ This calculates the length of the middle ordinate, M on the horizontal curve diagram.
        """
        if self.radius() and self.intersectangle():
            return (self.radius()*(1-np.cos((self.intersectangle()*(np.pi/180))/2)))

    def externaldist(self):
        """ This calculates the external distance, E on the horizontal curve diagram. This is not necessary for plotting
        the curve however it can be help if solving for PI, point of intersection.
        """
        if self.radius() and self.intersectangle():
            return (self.radius()*((1/np.cos((self.intersectangle()*(np.pi/180))/2)-1)))

    def solve(self):
        """ This calculates the coordinates for the middle of the curve which used be used to derive a formula
        for the parabola with the given coordinates and the calculated coordinates along the curve and at the point
        of tangent where the curve ends.
        """
        xcor1 = self.longchordlen()/2 + self.xcor
        ycor1 = self.ycor + self.midordlen()

        xcor2 = self.xcor + self.longchordlen()
        # ycor is equal to ycor2

        """ At this point we will transform the equation for a parabola to solve for a when we know the vertex (xcor1,ycor1)
        and two points along the curve (xcor,ycor).
        """

        a = (self.ycor-ycor1)/((self.xcor-xcor1)**2)

        xi = np.linspace(self.xcor,xcor2, 11)
        yi = a*(xi-xcor1)**2+ycor1

        plt.plot(xi, yi, color='#de2d26')

        plt.title('Horizontal Alignment Curve', fontweight='black', fontfamily='monospace')
        plt.xlabel('X (ft)')
        plt.ylabel('Y (ft)')
        plt.axis('equal')

        return plt.show()
    

 # -- Second class ---------------------------------------------------------------
class VerticalAlignment:

    driverreactiontime = 2.5 # Assumed, decription in README.md
    decelerationrate = 11.2 # Assumed, decription in README.md

    def __init__(self, xcor, zcor, g1, g2, speed, style):
        self.xcor = xcor
        self.zcor = zcor
        self.g1 = g1
        self.g2 = g2
        self.speed = speed
        self.style = style

    def sightdistance(self):
        """ This calculates stopping sight distance at the given velocity.
        """
        if self.speed and self.g1:
            return (1.47*self.speed*self.driverreactiontime)+((self.speed**2)/(30*(self.decelerationrate/32.2)+self.g1))

    def gradediff(self):
        """ This calculates the absolute value of difference in grades.
        """
        if self.g1 and self.g2:
            return np.abs(self.g1-self.g2)*100

    def curvelen(self):
        """ This calculates the horizontal length of the curve from according to standard criteria.
        """
        if self.style == 'crest':
            return (self.gradediff()*(self.sightdistance()**2))/(2158)
        elif self.style == 'sag':
            return (self.gradediff()*(self.sightdistance()**2))/(400+3.5*self.sightdistance())
        else:
            print('Invalid type of vertical curve. Choose sag or crest')

    def curvecheck(self):
        """ This check if the curve length is less than the stopping sight distance. If that is the
        case, new design equation are introduced to calculate a new length value.
        """
        if self.sightdistance() > self.curvelen():
            if self.style == 'crest':
                return (2*self.sightdistance())-(2158/self.gradediff())
            elif self.style == 'sag':
                return (2*self.sightdistance())-((400+3.5*self.sightdistance())/self.gradediff())
        else:
            return self.curvelen()

    def parabolaconstant(self):
        """ This calculates the parabola constant that can be used to graph the vertical curve
        """
        if self.g1 and self.g2 and self.curvecheck:
            return ((self.g2-self.g1)/(2*self.curvecheck()))


    def solve(self):
        """ This calculates the equation for the parabola given the parabola constant. The range of
        x-values in computed from the length of the curve.
        """
        xcor1 = self.xcor + self.curvelen()

        xi = np.linspace(self.xcor,xcor1, 11)
        zi = self.parabolaconstant()*(xi**2)

        plt.plot(xi, zi, color='#de2d24')

        plt.title('Vertical Alignment Curve', fontweight='black', fontfamily='monospace')
        plt.xlabel('X (ft)')
        plt.ylabel('Z (ft)')
        plt.axis('equal')

        return plt.show()
