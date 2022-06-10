def triangle_area(side_a, side_b, side_c):
    semiperimeter = (side_a + side_b + side_c) / 2
    area = (
        semiperimeter
        * (semiperimeter - side_a)
        * (semiperimeter - side_b)
        * (semiperimeter - side_c)
    ) ** 0.5

    return area


print(triangle_area(12, 14, 7))
