#  Write a Python program which accepts the radius of a circle from the user and computes area

from math import pi
r = float(input ("Input radius of circle : "))
print ("The area of the circle with radius"+str(r)+"is:"+str(pi * r**2))
