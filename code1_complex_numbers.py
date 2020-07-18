#!python3
"""
Complex numbers exercises from HackerRank
     https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/submissions/code/163464233


"""
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
     
    def __add__(self, no):
        imag = self.imaginary+no.imaginary
        if imag > -1e-6:
            return "%0.2f+%0.2fi"%(self.real+no.real,self.imaginary+no.imaginary)
        return "%0.2f%0.2fi"%(self.real+no.real,self.imaginary+no.imaginary)
     
    def __sub__(self, no):
        imag = self.imaginary-no.imaginary
        if imag > -1e-6:
            return "%0.2f+%0.2fi"%(self.real-no.real,self.imaginary-no.imaginary)
        return "%0.2f%0.2fi"%(self.real-no.real,self.imaginary-no.imaginary)
     
    def __mul__(self, no):
        imag = self.real*no.imaginary+self.imaginary*no.real
        if imag > -1e-6:
            return "%0.2f+%0.2fi"%(self.real*no.real-self.imaginary*no.imaginary,\
                             imag)
        return "%0.2f%0.2fi"%(self.real*no.real-self.imaginary*no.imaginary,\
                             imag)
     
    def __truediv__(self, no):
        no_amp = no.real*no.real + no.imaginary*no.imaginary
        imag = (-self.real*no.imaginary+self.imaginary*no.real)/no_amp
        if imag > -1e-6:
            return "%0.2f+%0.2fi"%((self.real*no.real+self.imaginary*no.imaginary)/no_amp,\
                                    imag)
        return "%0.2f%0.2fi"%((self.real*no.real+self.imaginary*no.imaginary)/no_amp,\
                               imag)
     
    def mod(self):
        import math
        return "%0.2f+0.00i"%math.sqrt(self.real*self.real +\
                                       self.imaginary*self.imaginary)
     
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

import math
print("input two complex numbers on two lines, in format REAL IMAG")
C = map(float, input().split())
D = map(float, input().split())
x = Complex(*C)
y = Complex(*D)
print('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))
#
