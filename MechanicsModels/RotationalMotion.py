############################################
#Constants

pi = 3.14

###########################################

'''Some formulas of mechanic :D '''
                #TakumiKun

class RotationalMotion():

    def angularVelocity(v, R):
        w = v / R
        print("Angular velocity of material point is " + str(w) + " sec^-1")

    def angularVelocityT(T):
        w = 2 * pi / T
        print("Angular velocity of material point is " + str(w) + " sec^-1")

    def angularAcceleration(w, t):
        '''1-Angular velocity, 2-time'''
        E = w / t
        print("Angular acceleration of material point is " + str(E) 
            + " sec^-2")

    def rotationFrequency(w, r):
        '''1-Angular velocity, 2-radius'''
        v = w * r
        print("Frequency of material point is " + str(v) + " hz")

    def centripetalAccelerationFrequency(w, v):
        '''1-Angular velocity, 2-Frequency'''
        a = w * v
        print("Centripetal acceleration of material point is "
             + str(a) + " m*sec^2")

    def centripetalAccelerationPeriod(R, T):
        '''1-Radius, 2-Period'''
        a = (4 * (pi ** 2) * R) / (T ** 2)
        print("Centripetal acceleration of material point is "
             + str(a) + " m*sec^2")
    
    def centripetalAccelerationVelocity(v, R):
        '''1-Velocity, 2-Radius'''
        a = v ** 2 / R
        print("Centripetal acceleration of material point is "
             + str(a) + " m*sec^2")
