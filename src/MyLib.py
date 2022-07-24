'''
Created on Jul 19, 2022

@author: max
'''

# StarceskiP9
# Programmer: Max Starceski 
# Email: mstarceski@cnm.edu
# Purpose: demonstrate how to define a class

import math

class GeoPoint:    
    def __init__(self, lat=0, lon=0,description = 'TBD'):
        self.lat = lat
        self.lon = lon
        self.description = description
    
    def SetPoint(self, point):
        self.lat = point[0]
        self.lon = point[1]
        
    def GetPoint(self):
        return (self.lat, self.lon)
    
    def Distance(self, toPoint):
        #Haversine formula:
        
        
        
        pointA = (math.radians(self.lat), math.radians(self.lon))
        pointB = (math.radians(toPoint.lat), math.radians(toPoint.lon)) 
        
        earthRadius = 6371
        
        sinArg1 = math.sin((pointA[0] - pointB[0])/2) 
        sinArg2 = math.sin((pointA[1] - pointB[1])/2) 
        
        factorA = math.pow(sinArg1, 2) + math.cos(pointA[0]) * math.cos(pointB[0]) * math.pow(sinArg2, 2)
        factorC = 2 * math.atan2(math.sqrt(factorA),math.sqrt(1 - factorA))
        
        distanceBetween = earthRadius * factorC 
        
        return distanceBetween
    
    def SetDescription(self, description):
        self.description = description
        
    def GetDescription(self):
        return self.description
    
    Point = property(GetPoint, SetPoint)
    
    Description = property(GetDescription, SetDescription)
    