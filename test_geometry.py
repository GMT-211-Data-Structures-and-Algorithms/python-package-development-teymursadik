import unittest
from geometry import Point

class TestGeometry(unittest.TestCase):
    def test_point_creation(self):
        # Bir nokta oluştur ve koordinatlarını kontrol et
        p = Point(1, 10.0, 20.0, "Test")
        self.assertEqual(p.x, 10.0)
        self.assertEqual(p.y, 20.0)
        self.assertEqual(p.label, "Test")

if __name__ == '__main__':
    unittest.main()