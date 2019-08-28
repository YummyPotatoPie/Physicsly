#############################################
#Astronomy and math constants

pi = 3.14

G = 6.67 * (10**(-11))
#Gravity const

au = 1.495978707 * (10**11)
#Astronomic Unit

S = 1.9818 * (10**30)
#Sun mass

M = 5.97 * (10**24)
#Earth mass

c = 299792458
#Speed of light

L = 3.827 * (10**26)
#Luminosity of Sun

h = 1.0545718 * (10**(-31))
#Planks const

k = 1.38064852 * (10**(-23))
#Bolcman const
#############################################

'''Black holes are intresting things. Mass of black holes 
        are expressed in Sun masses'''
                                #YuPie

class BlackHole():

    def gravityRadius(MassOfObject):
        '''Mass of object is exspressed in Sun masses'''
        r = (2*G*MassOfObject*S)/(c**2)
        print("Gravity radius of your black hole is " + str(r) + " m")

    def blackholeFluid(MassOfObject):
        '''Mass of object is exspressed in Sun masses'''
        fluid = (3*(c**6))/((32*pi)*(S*MassOfObject**2)*(G**3))
        print("Fluid of your black hole is " + str(fluid) + " kg/m^3")
        
    def blackholePower(MassOfBlackHole):
        '''Just enter mass of your black hole'''
        L_bh = (h * (c**6))/(15360*pi*(G**2)*(S*MassOfBlackHole**2))
        print("Power of black hole is " + str(L_bh) + " J*sec")

    def blackholeTemperature(MassOfBlackHole):
        '''Just enter mass of your black hole'''
        T = (h*(c**3))/(8*pi*G*MassOfBlackHole*S)
        print("Temperature of your black hole " + str(T) + " K")

    def blackholeEntropy(MassOfBlackHole):
        '''Enter black hole mass that needs 
                to find a gravity radius of your black hole'''
        r = (2*G*MassOfBlackHole*S)/(c**2) #Gravity radius
        A = 4*pi*(r**2) #Event horizon area  
        Ent = (A*k*(c**3))/(4*h*G) #Entropy of black hole
        print("Entropy of your black hole is " + str(Ent) + " J/K")

    def blackholeLifeTime(MassOfBlackHole):
        '''Just enter mass of your black hole'''
        t = (5120*pi*(G**2)*(S*MassOfBlackHole**3))/(h*(c**4))
        print("Life time of your black hole is " + str(t) + " sec")

    def complexAnalysBlackHole(MassOfBlackHole):
        '''Just enter mass of your black hole'''
        r = (2*G*MassOfBlackHole*S)/(c**2) #Gravity radius
        A = 4*pi*(r**2) #Event horizon area
        fluid = (3*(c**6))/((32*pi)*(S*MassOfObject**2)*(G**3)) #Fluid
        T = (h*(c**3))/(8*pi*G*MassOfBlackHole*S) #Temperature
        L_bh = (h * (c**6))/(15360*pi*(G**2)*(S*MassOfBlackHole**2))#Power
        Ent = (A*k*(c**3))/(4*h*G) #Entropy of black hole
        t = (5120*pi*(G**2)*(S*MassOfBlackHole**3))/(h*(c**4))#Life time
        print("Gravity radius of your black hole is " + str(r) + " m")
        print("Fluid of your black hole is " + str(fluid) + " kg/m^3")
        print("Power of black hole is " + str(L_bh) + " J*sec")
        print("Temperature of your black hole " + str(T) + " K")
        print("Entropy of your black hole is " + str(Ent) + " J/K")
        print("Life time of your black hole is " + str(t) + " sec")
