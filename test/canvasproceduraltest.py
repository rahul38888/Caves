import unittest

from scripts.algos.caveprocedural import CaveProcedural
from datahandler.layout import Layout


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        size = 10
        self.layout = Layout((size, size))
        self.cave_p = CaveProcedural(layout=self.layout)

    def test_all(self):
        self.cave_p.smoothing(iterations=2)
        for a in self.cave_p.layout.grid:
            print(list(map(lambda x: "#" if x else " ", a)))

        self.cave_p.detectRooms()
        self.cave_p.connectRooms()


if __name__ == '__main__':
    unittest.main()

