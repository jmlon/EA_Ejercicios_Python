#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------
# Point2DCartesian.py
# An implementation of the Point2D using the cartesian representation
#
# Author: Jorge Londoño
#-----------------------------------------------------------------------

import math
from point2D import Point2D
from point2DPolar import Point2DPolar 

class Point2DCartesian(Point2D):
    """Class representing points in the plane
    """

    def __init__(self, x:float, y:float):
        """Constructs a Point2D instance from the x,y coordinates
        """
        self._x = x
        self._y = y
        
    def __str__(self):
        """Returns a String representation of the point
        """
        return "("+str(self._x)+","+str(self._y)+")"
    
    def __abs__(self):
        """Returns the distance to the origin (magnitude)
        """
        return math.sqrt( self._x**2 + self._y**2 )
    
    def angle(self) -> float:
        """Returns the angle to the x axis
        """
        return math.atan2( self._y, self._x )
    
    def getX(self) -> float:
        """Returns the x component
        """
        return self._x

    def getY(self) -> float:
        """Returns the y component
        """
        return self._y
    

# Pruebas unitarias
if __name__=="__main__":
    p1 = Point2DCartesian(0,1)
    p2 = Point2DPolar(1,math.pi/2)
    p3 = Point2DCartesian(1,0)
    assert p1==p2, "p1 y p2 deben ser iguales"
    assert p2!=p3, "p2 y p3 deben ser distintos"
    assert p3!=p1, "p3 y p1 deben ser distintos"
    assert abs(p1)==1, "The norm of p1 must be 1"
    assert abs(p2)==1, "The norm of p2 must be 1"
    assert abs(p3)==1, "The norm of p3 must be 1"
    assert math.fabs(p1.distance(p3)-math.sqrt(2))<1e-12, "The distance beetween p1 and p3 must be sqrt(2)"