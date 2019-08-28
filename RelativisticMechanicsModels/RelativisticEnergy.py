##########################################
#Constants

c = 299792458
##########################################


'''Just some formulas of relativistic mechanics'''
                                            #YuPie

class RelativisticEnergy():

    def energyVelocity(V, m_0):
        '''Velocity must be lower then speed of light'''
        if V >= c:
            print("Incorrect velocity")
        else:
            m = m_0/(math.sqrt(1-((V**2)/(c**2))))
            E = m*(c**2)
            print("Relativistic of your object is " + str(E) + " J")

    def energyCalm(m):
        '''Just enter mass of your object'''
        E = m*(c**2)
        print("Relativistic of your object is " + str(E) + " J")
