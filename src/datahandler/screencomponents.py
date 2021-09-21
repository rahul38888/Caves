from enum import Enum


# Pre-defined points around the render coordinate
class Points(Enum):
    A = (-0.5, -0.5)
    B = (0, -0.5)
    C = (0.5, -0.5)
    D = (0.5, 0)
    E = (0.5, 0.5)
    F = (0, 0.5)
    G = (-0.5, 0.5)
    H = (-0.5, 0)


# triangles list mapped to each type of render points
coordinate_map = {
    # 0
    (0, 0, 0, 0): [],

    # 1
    (1, 0, 0, 0): [(Points.A.value, Points.B.value, Points.H.value)],
    (0, 1, 0, 0): [(Points.B.value, Points.C.value, Points.D.value)],
    (0, 0, 1, 0): [(Points.D.value, Points.E.value, Points.F.value)],
    (0, 0, 0, 1): [(Points.H.value, Points.F.value, Points.G.value)],

    # 2
    (1, 1, 0, 0): [(Points.A.value, Points.C.value, Points.D.value),
                   (Points.A.value, Points.D.value, Points.H.value)],
    (0, 1, 1, 0): [(Points.B.value, Points.C.value, Points.E.value),
                   (Points.B.value, Points.E.value, Points.F.value)],
    (0, 0, 1, 1): [(Points.H.value, Points.D.value, Points.E.value),
                   (Points.H.value, Points.E.value, Points.G.value)],
    (1, 0, 0, 1): [(Points.A.value, Points.B.value, Points.F.value),
                   (Points.A.value, Points.F.value, Points.G.value)],
    (1, 0, 1, 0): [(Points.A.value, Points.B.value, Points.H.value),
                   (Points.D.value, Points.E.value, Points.F.value)],
    (0, 1, 0, 1): [(Points.B.value, Points.C.value, Points.D.value),
                   (Points.H.value, Points.F.value, Points.G.value)],
    # (1, 0, 1, 0): [(Points.A.value, Points.B.value, Points.D.value),
    #                (Points.A.value, Points.D.value, Points.E.value),
    #                (Points.A.value, Points.E.value, Points.F.value),
    #                (Points.A.value, Points.F.value, Points.H.value)],
    # (0, 1, 0, 1): [(Points.B.value, Points.C.value, Points.D.value),
    #                (Points.B.value, Points.D.value, Points.F.value),
    #                (Points.B.value, Points.F.value, Points.G.value),
    #                (Points.B.value, Points.G.value, Points.H.value)],

    # 3
    (1, 1, 1, 0): [(Points.A.value, Points.C.value, Points.E.value),
                   (Points.A.value, Points.E.value, Points.F.value),
                   (Points.A.value, Points.F.value, Points.H.value)],
    (0, 1, 1, 1): [(Points.B.value, Points.C.value, Points.E.value),
                   (Points.B.value, Points.E.value, Points.G.value),
                   (Points.B.value, Points.G.value, Points.H.value)],
    (1, 0, 1, 1): [(Points.A.value, Points.B.value, Points.D.value),
                   (Points.A.value, Points.D.value, Points.E.value),
                   (Points.A.value, Points.E.value, Points.G.value)],
    (1, 1, 0, 1): [(Points.A.value, Points.C.value, Points.D.value),
                   (Points.A.value, Points.D.value, Points.F.value),
                   (Points.A.value, Points.F.value, Points.G.value)],

    # 4
    (1, 1, 1, 1): [(Points.A.value, Points.C.value, Points.E.value),
                   (Points.A.value, Points.E.value, Points.G.value)]
}
