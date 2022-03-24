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
    c = a.rot(10)

    assert round(c.a, 2) == 1.74
    assert round(c.b, 2) == 4.17

def test_normalize():
    a = Vec2d(3, 7)
    c = a.normalize()

    assert round(c.a, 2) == 0.39
    assert round(c.b, 2) == 0.92
    assert round(c.len()) == 1


