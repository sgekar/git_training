#!python3
"""
Find Torsional Angle from HackerRank
    https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem



    You are given four points and in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points and in degrees(not radians)

    Input Format
        One line of input containing the space separated floating number values
        of the X, Y, Z coordinates of a point.

    Output Format
        Output the angle correct up to two decimal places

"""
import math
class Point(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    #
    def vec3d(self,another_point):
        return Point(self.x - another_point.x, self.y - another_point.y, self.z
                - another_point.z)
    #
    def length(self):
        return math.sqrt(self.x *self.x + self.y*self.y + self.z*self.z)
    #
    def dot(self, another_vec):
        return math.sqrt(self.x*another_vec.x+self.y*another_vec.y+\
                   self.z*another_vec.z)
    #
    def cross(vec3d_A, vec3d_B):
        return Point(vec3d_A.y * vec3d_B.z, -(vec3d_A.x * vec3d_B.z), vec3d_A.x *\
                vec3d_B.y)
    #
    def __str__(self):
        return("{0},{1},{2}".format(self.x,self.y,self.z))
#
#
#
if __name__== '__main__':
    #
    print('\n\n\nInput 4 points on 4 lines seperate lines, each line in format X Y Z\n')
    components = map(float, input().split())
    pt_A = Point(*components)
    print(str(pt_A))
    components = map(float, input().split())
    pt_B = Point(*components)
    print(str(pt_B))
    components = map(float, input().split())
    pt_C = Point(*components)
    print(str(pt_C))
    components = map(float, input().split())
    pt_D = Point(*components)
    print(str(pt_D))
    #
    vec_AB = pt_A.vec3d(pt_B)
    vec_BC = pt_B.vec3d(pt_C)
    vec_CD = pt_C.vec3d(pt_D)
    X = vec_AB.cross(vec_BC)
    Y = vec_BC.cross(vec_CD)
    print('angle = {}'.format(180.0*math.acos(X.dot(Y) / \
                                         X.length() / Y.length()/math.pi)))

#
