
def triangle_area(side_a, side_b, side_c):
    side = (side_a + side_b + side_c) / 2
    area = (side * (side - side_a) * (side - side_b) * (side - side_c)) ** 0.5

    return area


print(triangle_area(12, 14, 7))
