##############################
                            #TakumiKun


class Motion():

    def accelerationTime(v, v_0, t):
        '''1-velocity, 2-velocity_0, 3-time'''
        a = (v-v0)/t
        print("Acceleration is " + str(a) + " m/sec^2")

    def accelerationDestination(v, v_0, S):
        '''1-velocity, 2-velocity_0, 3-destination'''
        a = (v**2 - v_0**2)/(2*S)
        print("Acceleration is " + str(a) + " m/sec^2")

    def destination(v,t,a):
        '''1-velocity, 2-time, 3-acceleration'''
        S = (v_0*t)+(a*t**2)/2
        print("Destination is " + str(a) + " m")

    def velocity(a, v_0, t):
        '''1-acceleration, 2-velocity_0, 3-time'''
        v = v_0 + a*t
        print("Velocity is " + str(v) + " m per second")


