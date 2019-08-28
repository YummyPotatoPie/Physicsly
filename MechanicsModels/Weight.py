##############################
#Constants

g = 9.80666

##############################
                            #TakumiKun
class Weight():

    def weightPeace(m):
        '''in peace'''
        p = m * g
        print("Weight of your object is " + str(p) + " N")

    def weightDown(m, a):
        '''the prop is accelerating down
                arguments: 1-mass, 2-acceleration'''
        p = m * (g + a)
        print("Weight of your object is " + str(p) + " N")

    def weightUp(m, a):
        '''the prop is accelerating up
                arguments: 1-mass, 2-acceleration'''
        p = m * (g - a)
        print("Weight of your object is " + str(p) + " N")

    def weightConvex(m, v, r):
        '''the prop is moving along a convex path
                arguments: 1-mass, 2-velocity, 3-radius'''
        p = m * (g - (v**2) / r)
        print("Weight of your object is " + str(p) + " N")

    def weightConcave(m, v, r):
        '''the prop is moving along a concave path
                arguments: 1-mass, 2-velocity, 3-radius'''
        p = m * (g + (v**2) / r)
        print("Weight of your object is " + str(p) + " N")