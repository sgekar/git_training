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

    def vec3d(self,another_point):
        return self.x - another_point.x, self.y - another_point.y, self.z - another_point.z

    def vec3d_length(self):
        return math.sqrt(self.x *self.x + self.y*self.y + self.z*self.z)

    def vec3d_dot(self, another_vec):
        return (math.sqrt(self.x*another_vec.x),math.sqrt(self.y*another_vec.y),\
                   math.sqrt(self.z*another_vec.z))

    def vec3d_cross(vec3d_A, vec3d_B):
        return (vec3d_A.y * vec3d_B.z, -(vec3d_A.x * vec3d_B.z), vec3d_A.x *\
                vec3d_B.y)
#
#
#
if __name__== '__main__':
    #
    print('\n\n\nInput 4 points on 4 lines seperate lines, each line in format X Y Z\n')
    line_in= input()
    pt_A = line_in.split()
    line_in= input()
    pt_B = line_in.split()
    line_in = input()
    pt_C = line_in.split()
    line_in = input()
    pt_D = line1.split()
    #
    X = vec3d_cross(vec3d(pt_A,pt_B), vec3d(pt_B,pt_C))
    Y = vec3d_cross(vec3d(pt_B,pt_C), vec3d(pt_C,pt_D))
    print('angle = {}'.format(math.acos(vec3d_dot(X,Y) / \
                                         vec3d_length(X) / vec3d_length(Y))))

#
