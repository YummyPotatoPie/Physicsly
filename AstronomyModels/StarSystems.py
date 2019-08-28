import math
#############################################
#Astronomy constants

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
#############################################


'''Mass of planets are expressed in Earth masses, 
        mass of stars are expressed in Sun masses, destination 
        and semimajor axes are expressed in billions kilometers'''
                                                            #YuPie

class StarSystemModel():

    def acceleration(Mass, Radius):
        '''for correct result you must enter mass of 
                planet first and radius second'''
        a_m = ((Mass*M) * G)/(Radius**2)
        print("Acceleration on this planet: " + str(a_m) + " m/s^2")

    def firstSpaceVelocity(Mass):
        '''Mass is expressed in Earth masses'''
        speed = math.sqrt(Mass*M*G)
        print("First space velocity oon your planet is " + str(speed) + " m/s")

    def gravityForce(Mass_planet, Mass_star, Destination):
        '''for correct result you must enter mass of 
                planet first, mass of star second
                    and destination to their centers third'''
        gforce = float(G * (Mass_planet*M) * (Mass_star*S))/(Destination**2)
        print("Gravity is " + str(gforce) + " N")

    def orbitalSpeed(MassObject, MassStar, SemimajorAxis, Destination):
        '''first value is mass of first object, second is 
            mass of second object, next is semimajor axis and 
                destination between objects'''
        GravityParametr = float(G *((MassObject*M) + (MassStar*S)))
        OrbitalEnergy = float(-GravityParametr/(SemimajorAxis*(10**9)))
        OrbitalSpeed = float(math.sqrt(2 * (GravityParametr/Destination)
            + OrbitalEnergy))
        print("Orbital speed of this object is " + str(OrbitalSpeed) + "m/s")

    def habitableArea(StarPower, Luminosity):
        '''Power of star are exspressed in Sun powers,
                luminosity are expressed in Sun luminosity'''
        HZ = math.sqrt(au * StarPower)
        dAU = math.sqrt((Luminosity*L)/L)
        print("Destination of habitable zone is " + str(HZ) + "AU")
        print("Diameter of habitable zone is " + str(dAU) + "AU")

    def supernova(MassOfStar):
        '''Just enter mass of your star'''
        if (MassOfStar*S) <= S*8:
            print("After supernova your star will become white dwarf")
        elif (S*8) < (MassOfStar*S) < (S*20):
             print("After supernova your star will become neutron star")
        elif MassOfStar >= (S*20):
            print("After supernova your star will become black hole")
