from vec2d import Vec2d


def test_sum():
    a = Vec2d(3, 7)
    b = Vec2d(4, 5)

    c = a + b
    assert c.a == 7
    assert c.b == 12


def test_sub():
    a = Vec2d(3, 7)
    b = Vec2d(4, 5)

    c = a - b
    assert c.a == -1
    assert c.b == 2

def test_rot():
    a = Vec2d(3, 7)
    c = a.rot(100)

    assert round(c.a, 2) == -7.33
    assert round(c.b, 2) == 6.55

def test_normalize():

    pass