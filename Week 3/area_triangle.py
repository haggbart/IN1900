# 3.16 (area_triangle.py, side 134)

def test_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = ('computed area=%g !=%g (expected)' % \
    (computed, expected))
    assert success, msg

def triangle_area(vertices):
    A = 1/2*abs(vertices[1][0] * vertices[2][1] -
                vertices[2][0] * vertices[1][1] -
                vertices[0][0] * vertices[2][1] +
                vertices[2][0] * vertices[0][1] +
                vertices[0][0] * vertices[1][1] -
                vertices[1][0] * vertices[0][1])
    return A



v1 = (0,0)
v2 = (10,0)
v3 = (0,10)
vertices = [v1,v2,v3]


print(triangle_area(vertices))
print(test_triangle_area())

"""
Terminal> area_triangle.py"
50.0
None

Process finished with exit code 0
"""