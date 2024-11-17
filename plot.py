'''
plot to show atoms for laue diffraction. Salma Garcia.
'''
from matplotlib import pyplot as plt
import numpy as np

class Setup:
    def __init__(self,interatomic_spacing,xray_angle):
        '''
        distances in ångstroms
        '''
        self.i_s=interatomic_spacing
        self.x_a=xray_angle
        self.radius=1.5/10
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()

    def _drawatoms(self):
        self.atom1 = [0,0]
        self.atom2 = [0,self.i_s]
        circle1 = plt.Circle(self.atom1,self.radius)
        circle2 = plt.Circle(self.atom2,self.radius)
        for circle in [circle1,circle2]:
            self.ax.add_patch(circle)

    def _getbound(self):
        self.xmin = self.atom1[0]-self.i_s
        self.xmax = self.atom1[0]+self.i_s
        self.ymin = self.atom1[1]-self.i_s/2
        self.ymax = self.atom2[1]+self.i_s/2

    def _getaxislimits(self):
        self.ax.set_xlim(self.xmin,self.xmax)
        self.ax.set_ylim(self.ymin,self.ymax)

    def _getxray(self):
        self.xray = [np.sin(self.x_a), np.cos(self.x_a)]

    def _plotxray(self):
        self.ax.arrow(0,0,self.xray[0],self.xray[1])

"""
This is the unit vector
"""

test = True
if test == True:
    s = Setup(1.42,22.5)
    s._drawatoms()
    s._getbound()
    s._getaxislimits()
    s._getxray()
    s._plotxray()
    plt.show()