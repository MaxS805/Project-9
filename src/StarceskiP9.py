# StarceskiP9
# Programmer: Max Starceski 
# Email: mstarceski@cnm.edu
# Purpose: demonstrate how to define a class

from MyLib import GeoPoint 
'''
class GeoPoint:    
    def __init__(self):
        self.lat = 0
        self.lon = 0
        self.description = "TBD"
    
    def SetPoint(self, point):
        self.lat = point[0]
        self.lon = point[1]
        
    def GetPoint(self):
        return (self.lat, self.lon)
    
    def Distance(self, toPoint):
        #Haversine formula:
        
        
        
        pointA = (math.radians(self.lat), math.radians(self.lon))
        pointB = (math.radians(toPoint[0]), math.radians(toPoint[1])) 
        
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
    
    '''
    
    
    


khufuPyramid = GeoPoint(29.978909212798886, 31.1334508788751, "Large Egyptian triangle") 
'''
khufuPyramid.SetPoint(29.978909212798886, 31.1334508788751)

khufuPyramid.SetDescription("Large Egyptian triangle")
'''
gundam = GeoPoint()
gundam.Point = 35.44746394107316, 139.65447644830985
gundam.Description = "Large Japanese robot"
'''
gundam.SetPoint(35.44746394107316, 139.65447644830985)

gundam.SetDescription("Large Japanese robot")
'''






doAnother = 'y'
while doAnother == 'y':
    '''
    try:
        print("Enter your coordinates: ")
        
        lat = float(input("Enter your latitude: "))
        
        lon = float(input("Enter your longitude: "))
        
        pointUser = GeoPoint(lat,lon, 'User Location') 
        
        distanceToOne = khufuPyramid.Distance(pointUser)
        
        distanceToTwo = gundam.Distance(pointUser)
        
        if (distanceToOne == distanceToTwo):
            print("You are equidistant to the ", khufuPyramid.GetDescription(), " located at", khufuPyramid.GetPoint(), "and the", gundam.GetDescription(), "located at", gundam.GetPoint())
        elif (distanceToOne < distanceToTwo):
            print("You are closer to", khufuPyramid.GetDescription(), "at", khufuPyramid.GetPoint())
        else:
            print("You are closer to", gundam.GetDescription(), "at", gundam.GetPoint())
        
        
    except TypeError :
        print("Wrong type of input!")
    except ArithmeticError  :
        print("The values you entered caused an arithmetic error, consult the author for further information")
    except Exception as e:
        print("Something went wrong: ", e)
    '''
     
    print("Enter your coordinates: ")
        
    lat = float(input("Enter your latitude: "))
    
    lon = float(input("Enter your longitude: "))
    
    pointUser = GeoPoint(lat, lon, 'User Location') 
    
    #print(pointUser.lat)
    
    
    distanceToOne = khufuPyramid.Distance(pointUser)
    
    distanceToTwo = gundam.Distance(pointUser) 
    
    if (distanceToOne == distanceToTwo):
        print("You are equidistant to the ", khufuPyramid.GetDescription(), " located at", khufuPyramid.GetPoint(), "and the", gundam.GetDescription(), "located at", gundam.GetPoint())
    elif (distanceToOne < distanceToTwo):
        print("You are closer to", khufuPyramid.GetDescription(), "at", khufuPyramid.GetPoint())
    else:
        print("You are closer to", gundam.GetDescription(), "at", gundam.GetPoint())
    
    
    doAnother = input("Do another (y/n)? ")     



    
print("Goodbye")

