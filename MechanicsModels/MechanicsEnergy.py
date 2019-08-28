##############################
#Constants

g = 9.80666

##############################
                            #TakumiKun


class MechanicsEnergy():

    def potentialEnergy(m, h):
        E = m * g * h
        print("Potential energy is " + str(E) + " J")

    def kineticEnergy(m, v):
        E = (m * v ** 2) / 2
        print("Kinetic energy is " + str(E) + " J")

    def mechanicsEnergy(m, h, v):
        '''1-mass, 2-height, 3-velocity'''
        E = (m * g * h) + (m * v ** 2) / 2
        print("Potential energy is " + str(E) + " J")
