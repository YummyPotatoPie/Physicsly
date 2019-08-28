###############################
#Constants

Absolute_Zero = -273
###############################

'''The module uses only Kelvin if you want to use 
        degrees Celsius or use special definition'''
                                            #YuPie

class Thermal():

    def quantityOfHeatK(K, m, hc):
        '''Enter heat first, mass second and heat capacity third'''
        Q = hc*m*K
        print("Quantity of heat is " + str(Q) + " J")
    
    def quantityOfHeatC(C, m, hc):
        '''Enter heat first, mass second and heat capacity third'''
        K = C+Absolute_Zero
        Q = hc*m*K
        print("Quantity of heat is " + str(Q) + " J")

    def quantityOfHeatF(F, m, hc):
        '''Enter heat first, mass second and heat capacity third'''
        C = (F-32)/1.8
        K = C+Absolute_Zero
        Q = hc*m*K
        print("Quantity of heat is " + str(Q) + " J")

class ThermalT_0():

    def quantityOfHeatK(m, hc, T_0, T):
        '''Enter mass first, heat capacity second 
                and temperatures'''
        Q = hc*m*(T-T_0)
        print("Quantity of heat is " + str(Q) + " J")
    
    def quantityOfHeatC(m, hc, T_0, T):
        '''Enter mass first, heat capacity second 
                and temperatures'''
        T = T+Absolute_Zero
        T_0 = T_0+Absolute_Zero
        Q = hc*m*(T-T_0)
        print("Quantity of heat is " + str(Q) + " J")

    def quantityOfHeatF(m, hc, T_0, T):
        '''Enter mass first, heat capacity second 
                and temperatures'''
        T = (T-32)/1.8
        T_0 = (T_0-32)/1.8
        T = T+Absolute_Zero
        T_0 = T_0+Absolute_Zero
        Q = hc*m*(T-T_0)
        print("Quantity of heat is " + str(Q) + " J")
