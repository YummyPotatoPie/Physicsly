################################
#Constants

e0 = 8.85 * (10**(-12))
#dielectric permittivity

pi = 3.14
################################

class ElectricField():

    def pendantLaw(q1,q2,e,r):
        '''1,2-point charges, 
            3-dielectric permittivity, 4- radius'''
        F = (q1*q2)/(4*pi*e0*e*(r**2))
        print("Force is " + str(F) + " N")

    def electricFieldStrength(F,q):
        '''Enter force and charge'''
        E = F/q
        print("Strength is " + str(E) + " N/q")

    def electricFieldPotential(W,q):
        '''potential energy and charge'''
        f = W/q
        print("Potential is " + str(f) + " V")

