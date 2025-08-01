import math

big_G = float(6.67428e-11)
#Choice 1
def height_FROMSPEED():
    mass_ONE = float(input("Mass of the central body in kg (scientific notation): "))
    radius_ONE = float(input("Radius of the central body in meters (scientific notation): "))
    speed_TWO = float(input("Speed of the satellite body in meters per second: "))
    
    radius = (big_G*mass_ONE)/(speed_TWO**2)
    height = round((radius-radius_ONE)/1000, 4)
    
    return str(height)

def speed_FROMHEIGHT():
    mass_ONE = float(input("Mass of the central body in kg (scientific notation): "))
    radius_ONE = float(input("Radius of the central body in meters (scientific notation): "))
    height_TWO = float(input("Orbital height of the satellite body in meters (scientific notation): "))
    
    speed = round(math.sqrt((big_G*mass_ONE)/(radius_ONE+height_TWO)), 4)
    return str(speed)

def period_ORBIT():
    mass_ONE = float(input("Mass of the central body in kg (scientific notation): "))
    radius_ONE = float(input("Radius of the central body in meters (scientific notation): "))
    height_TWO = float(input("Orbital height of the satellite body in meters (scientific notation): "))
    
    period = round((2*math.pi)*math.sqrt(((radius_ONE+height_TWO)**3)/(big_G*mass_ONE))/3600, 4)
    return str(period)