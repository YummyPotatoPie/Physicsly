##########################################
#Constants

c = 299792458
##########################################


'''Just some formulas of relativistic mechanics'''
                                            #YuPie

class RelativisticForce():

    def relativisitcForce(V, m, t):
        '''First argument is velosity,
                second is mass of object,
                    third is time'''
        if V >= c:
            print("Incorrect velocity")
        else:
            F = (m*V)/(t*math.sqrt(1-((v**2)/(c**2))))
            print("Relativistic froce is " + str(F) + " N")

    def relativisiticPulse(V, m_0):
        '''First argument is velocity
            second is mass'''
        if V >= c:
            print("Incorrect velocity")
        else:
            p =(m*V)/(math.sqrt(1-((v**2)/(c**2))))
            print("Pulse of your object " + str(p) + " N")

    def relativisticCinetic(V,m_0):
        '''First argument is velocity
            second is mass'''
        if V >= c:
            print("Incorrect velocity")
        else:
            m = m_0/(math.sqrt(1-((V**2)/(c**2))))
            T = (m*(c**2))/(math.sqrt(1-((v**2)/(c**2))))
            print("Cinetic energy of your object is " + str(T) + " J")
