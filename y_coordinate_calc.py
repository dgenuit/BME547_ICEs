def y_coord_calc(Point_1, Point_2, new_x):
    slope = (Point_1[1] - Point_2[1])/(Point_1[0] - Point_2[0])
    intercept = Point_1[1] - slope * Point_1[0]
    new_y = slope * new_x + intercept
    return new_y
