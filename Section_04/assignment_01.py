# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

# Your Code Below:

def twelver(a,b):
    if(((a == 12) or (b == 12)) or ((a+b) == 12)):
        return True
    else:
        return False


r1 = twelver(3,12)
r2 = twelver(4,9)
r3 = twelver(9,3)
print(r1, r2, r3)





































# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)
