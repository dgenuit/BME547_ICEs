import pytest

@pytest.mark.parmetrize("Point_1, Point2, new_x, expected_y_coord", [
    ((1, 1), (2, 2), 3, 3),
    ((2, 6), (10, 10), -12, -1),
    ((-1, 1), (4, -9), 0, -1)
    ])
def test_y_coord_calc(Point_1, Point_2, new_x, expected_y_coord):
    from y_coordinate_calc import y_coord_calc
    answer = y_coord_calc(Point_1, Point_2, new_x)
    expected = expected_y_coord
    assert answer == expected