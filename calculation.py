import numpy as np


# line1_Y1, line1_Z1 = (float(i.replace(',', '')) for i in line1_Y1_Z1.split(' '))
# line1_Y2, line1_Z2 = (float(i.replace(',', '')) for i in line1_Y2_Z2.split(' '))
# line2_Y1, line2_Z1 = (float(i.replace(',', '')) for i in line2_Y1_Z1.split(' '))
# line2_Y2, line2_Z2 = (float(i.replace(',', '')) for i in line2_Y2_Z2.split(' '))
# line3_Y1, line3_Z1 = (float(i.replace(',', '')) for i in line3_Y1_Z1.split(' '))
# line3_Y2, line3_Z2 = (float(i.replace(',', '')) for i in line3_Y2_Z2.split(' '))
#
# line1 = [[line1_Y1, line1_Z1], [line1_Y2, line1_Z2]] # координаты точек первой линии
# line2 = [[line2_Y1, line2_Z1], [line2_Y2, line2_Z2]]       # координаты точек второй линии
# line3 = [[line3_Y1, line3_Z1], [line3_Y2, line3_Z2]]  # координаты точек третьей линии

line1 = [[-90, 10.520], [90, 10.510]]  # координаты точек первой линии
line2 = [[-5.150, 0], [99, 60]]        # координаты точек второй линии
line3 = [[21.650, 0], [81.150, 100]]   # координаты точек третьей линии


def line_eq(x1, y1, x2, y2):
    """line Y-coord and a, b coeffs"""
    if x1 - x2:
        a = (y1 - y2) / (x1 - x2)
    else:
        a = 0
    b = y2 - a * x2
    return (a * x + b, a, b)


def cross_lines(a1, a2, b1, b2):
    """cross point coordinates function"""
    M1 = np.array([[-a1, 1.], [-a2, 1.]])  # matrix (left part)
    v1 = np.array([b1, b2])  # vector (right part)
    return np.linalg.solve(M1, v1)


def line_length(x0, y0, x1, y1):
    """line length function"""
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5


x = np.arange(-50, 50, 0.05)

# first line
x10, y10, x11, y11 = line1[0][0], line1[0][1], line1[1][0], line1[1][1]
Y1, a1, b1 = line_eq(x10, y10, x11, y11)

# second line
x20, y20, x21, y21 = line2[0][0], line2[0][1], line2[1][0], line2[1][1]
Y2, a2, b2 = line_eq(x20, y20, x21, y21)

# third line
x30, y30, x31, y31 = line3[0][0], line3[0][1], line3[1][0], line3[1][1]
Y3, a3, b3 = line_eq(x30, y30, x31, y31)

# cross_point Y1_Y2
x_a, y_a = cross_lines(a1, a2, b1, b2)

# cross_point Y1_Y3
x_b, y_b = cross_lines(a1, a3, b1, b3)

# cross_point Y2_Y3
x_c, y_c = cross_lines(a2, a3, b2, b3)

# AB, AC, BC lengths
a_b = line_length(x_a, y_a, x_b, y_b)
a_c = line_length(x_a, y_a, x_c, y_c)
b_c = line_length(x_b, y_b, x_c, y_c)

# F-point coordinates on AC line
x_f = (x_a + (a_b / b_c) * x_c) / (1 + (a_b / b_c))
y_f = (y_a + (a_b / b_c) * y_c) / (1 + (a_b / b_c))

# Bisector 1
Y_b1, a_b1, b_b1 = line_eq(x_b, y_b, x_f, y_f)

# Create point E on line1
x_e, y_e = (0, a1 * 0 + b1)

# AE lengths
a_e = line_length(x_a, y_a, x_e, y_e)

# K-point coordinates on EC line
x_k = (x_e + (a_e / a_c) * x_c) / (1 + (a_e / a_c))
y_k = (y_e + (a_e / a_c) * y_c) / (1 + (a_e / a_c))

# Bisector 2
Y_b2, a_b2, b_b2 = line_eq(x_a, y_a, x_k, y_k)

# cross_point of bisectors
x_cross_b, y_cross_b = cross_lines(a_b1, a_b2, b_b1, b_b2)

# circle radius
r = abs(((x_a - x_c) * (y_cross_b - y_c) - (y_a - y_c) * (x_cross_b - x_c)) / line_length(x_a, y_a, x_c, y_c))

# округление радиуса
r_round = 3
# округление координаты x
x_round = 8
# округление координаты y
y_round = 8

print(f'Радиус: {round(r, r_round)}, y: {round(x_cross_b, x_round)}, z: {round(y_cross_b, y_round)}')
