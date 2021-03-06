#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

def isAtriangle(a, b, c):
    return True

# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    try:
        if min([a, b, c]) <= 0:
            raise TriangleError, "Bad input"
        x,y,z = sorted([a,b,c])
        if x+y<=z:
            raise TriangleError,"short side"
        if a == b and a == c and b == c:
            return 'equilateral'
        if a == b or a == c or b == c:
            return 'isosceles'
        else:
            return 'scalene'
    except:
        raise TriangleError('not a triangle')


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
