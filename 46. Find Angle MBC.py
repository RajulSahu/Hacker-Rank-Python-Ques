import math

AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2 + BC**2)

angle_MBC = str(round(math.degrees(math.acos(BC/AC))))+ chr(176)
print(angle_MBC)

