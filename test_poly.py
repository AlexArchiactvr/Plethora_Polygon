import unittest
import numpy as np
from polygon import polygon
from polygon import isValid


class PolygonTestCase(unittest.TestCase):

	def test_valid_poly(self):
		valid_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)], 
						[(-10.2, -6), (0, 0), (1, -3), (1, -7), (0, -4), (-10.2, -6)]]
		for poly in valid_polys:
			self.assertTrue(isValid(poly))

	def test_invalid_poly(self):
		invalid_polys = [[(0, 0), (1, 0), (0, 0)],
							[(0, 0), (1, 0), (1, 1), (0.5, 1), (0.5, 0), (0, 0)],
							[(0, 0), (1, 0), (1, 1), (0, 0), (-1, 0), (0, -1), (0, 0)],
							[(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]]
		for poly in invalid_polys:
			self.assertFalse(isValid(poly))

	def test_perimeter(self):		
		perim_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
							[(0,0),(2,0),(5,4),(2,8),(-1,4),(0,4),(0,0)],
							[(0,0),(-4,-3),(-1,1),(0,0)]]
		perim_values = [4,22,10+np.sqrt(2)]

		for ni, poly in enumerate(perim_polys):
			test_poly = polygon(poly)
			self.assertEqual(perim_values[ni],test_poly.perimeter())

	def test_area(self):
		area_polys= [[(0,0),(3,0),(3,4),(0,0)],
						[(0,0),(3,4),(3,6),(-1,9),(-1,0),(0,0)],
						[(0,0),(1,0),(1,1),(3,1),(3,0),(5,0),(5,5),(0,5),(0,0)]]
		area_values = [6,24,23]
		for na, poly in enumerate(area_polys):
				test_poly = polygon(poly)
				self.assertEqual(area_values[na],test_poly.area())

if __name__ == '__main__':
	unittest.main()