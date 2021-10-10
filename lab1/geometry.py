### Основные функции
def is_correct_triangle(A, B, C):
    line12 = line_equation(A, B)
    line23 = line_equation(B, C)
    return matrix_det(line12[0], line12[1], line23[0], line23[1])


def line_len(A, B):
    return ((A['x'] - B['x'])**2 + (A['y'] - B['y'])**2)**0.5


def line_equation(M, N):
    A = N['y'] - M['y']
    B = M['x'] - N['x']
    C = -M['x'] * A - M['y'] * B
    return A, B, C


def find_cross(A1, B1, C1, A2, B2, C2):
    P = {}
    print(A1, B1, C1,  A2, B2, C2)
    z = matrix_det(A2, B2, A1, B1)
    P['x'] = -matrix_det(C2, B2, C1, B1) / z
    P['y'] = -matrix_det(A2, C2, A1, C1) / z
    return P


def matrix_det(a, b, c, d):
    return a * d - b * c


### Функции поиска
# Поиск CH
def find_height(AB, BC, CA):
    p = (AB + BC + CA) / 2
    return 2/AB * (p*(p-AB)*(p-BC)*(p-CA))**0.5


# Поиск треугольник с максимальной высотой
def find_max_height(points):
    n = len(points)
    max_h = None
    max_triangle = None

    for A in range(n):
        for B in range(A + 1, n):
            AB = line_len(points[A], points[B])
            for C in range(B + 1, n):
                if (not is_correct_triangle(points[A], points[B], points[C])):
                    continue

                AC = line_len(points[A], points[C])
                BC = line_len(points[B], points[C])
                min_line = min(AB, BC, AC)

                if (min_line == AB):
                    h = find_height(AB, BC, AC)
                    triangle = [C, A, B]
                elif (min_line == AC):
                    h = find_height(AC, AB, BC)
                    triangle = [B, A, C]
                else:
                    h = find_height(BC, AC, AB)
                    triangle = [A, B, C]

                if (max_h is None or max_h < h):
                    max_h = h
                    max_triangle = triangle

                print(h)
    return max_h, max_triangle


# Поиск координат точки H (MH - высота)
def find_h_xy(M, N, K):
    print(M, N, K)
    A_1, B_1, C_1 = line_equation(N, K)     # Линия NK
    A_2, B_2 =  -B_1, A_1
    C_2 = A_2*(-M['x']) + B_2*(-M['y'])     # Линия MH
    return find_cross(A_1, B_1, C_1, A_2, B_2, C_2)



