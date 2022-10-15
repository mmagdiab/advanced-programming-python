from math import sin, cos, radians

for i in range(0, 350, 15):
    print(i, '----', round(sin(radians(i)), 4), round(cos(radians(i)), 4))