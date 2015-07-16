import numpy as np

class polygon:

	def __init__(self, verts):
		if(isValid(verts)):
			self.verts = verts

	def perimeter(self):
		perim = 0
		for a,b in zip(self.verts[:-1], self.verts[1:]):
			temp = np.subtract(a,b)
			perim += np.sqrt(np.dot(temp,temp))
		return perim

	def area(self):
		area = 0
		#use the origin as a base point
		#in incremental pairs calculate the area of
		#the triangle formed from by the origin, and the
		#other two points on the polygon.
		#the extra area will naturally be subtracted
		#when calculating the area of triangles on the
		#origin-side of the polygon.
		for a,b in zip(self.verts[:-1], self.verts[1:]):
			area += np.cross(a, b)
		return np.absolute(area*0.5)

	def transform(self, matrix):
		zw = (0,1)
		res = [matrix.dot(np.array(vert+zw))for vert in self.verts]
		w = res[0].item(3)
		return [tuple(ver.getA()[0][:-2]/w) for ver in res]

def isValid(verts):
	#adjacent lines can only meet once
	#next-nearest lines and beyond cannot intersect at all.

	#check every adjacent line
	#considering the parametric equations. we cannot allow
	#a relationship between t_1 and t_2
	#L_1 = a + t_1(b-a)
	#L_2 = c + t_2(d-c)
	#L_1 = L_2
	#a + t_1(b-a) = c +t_2(d-c)
	#let b-a = B, let d-c = D
	#B*Binv = 0
	#Binv = (-B_y, B_x)
	#a*Binv = c*Binv + t_2(D*Binv)

	#t_2 = (a-c)*Binv / (D*Binv)
	#let A = a-c
	#we expect t_2 = 0 for adjacent sides
	#if 0<=t_2<=1 for any other side, then there is an intersection
	for ni, i in enumerate(verts[:-2]):
		for nj, j in enumerate(verts[ni+1:-1]):
			nj += ni + 1
			D = np.subtract(verts[nj+1],j)
			B = np.subtract(verts[ni+1],i)
			Binv = (-B[1], B[0])
			A = np.subtract(i,j)

			DBinv = np.dot(D,Binv)

			if DBinv != 0:
				t2 = np.dot(A,Binv)/DBinv
				t1 = np.dot(t2*D - A, B)/np.dot(B,B)
				if (nj-ni == 1) : #adjacent sides (not necessary)
					if t2 != 0:
						return False
				elif nj-ni == len(verts)-2: #end and start are adjacent
					if t2 != 1:
						return False
				else:
					if (t2 >=0 and t2 <=1) and (t1 >=0 and t1 <=1):
						return False
			elif np.dot(A,Binv) == 0: #can be parallel, but not overlapping
				#a + t_1(b-a)  = c +t_2(d-c)
				#t1 = (-A + t2D) / B
				#check t2 = 0, and t2 = 1
				magB= np.dot(B,B)
				t1_0 = -np.dot(A,B)/magB	#(-A*B)/(B*B)
				t1_1 = np.dot(np.subtract(D,A),B)/magB	#(-A + D)*B/(B*B)

				if (t1_0 >= 0 and t1_0 <= 1) or (t1_1 >=0 and t1_1 <=1):
					return False
	return True

def main():
	valid_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
					[(-10.2, -6), (0, 0), (1, -3), (1, -7), (0, -4), (-10.2, -6)],
					[(0,0),(1,0),(1,1),(3,1),(3,0),(5,0),(5,5),(0,5),(0,0)]]
	invalid_polys = [[(0, 0), (1, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0.5, 1), (0.5, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0, 0), (-1, 0), (0, -1), (0, 0)],
						[(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]]
	for poly in valid_polys:
		polygon(poly)
	for poly in invalid_polys:
		polygon(poly)

	print "Perimeters"
	perim_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
						[(0,0),(2,0),(5,4),(2,8),(-1,4),(0,4),(0,0)],
						[(0,0),(-4,-3),(-1,1),(0,0)]]
	perim_values = [4,22,10+np.sqrt(2)]

	for ni, poly in enumerate(perim_polys):
		test_poly = polygon(poly)
		print perim_values[ni] == test_poly.perimeter()

	print "Areas"
	area_polys= [[(0,0),(3,0),(3,4),(0,0)],
					[(0,0),(3,4),(3,6),(-1,9),(-1,0),(0,0)],
					[(0,0),(1,0),(1,1),(3,1),(3,0),(5,0),(5,5),(0,5),(0,0)]]
	area_values = [6,24,23]
	for ni, poly in enumerate(area_polys):
		test_poly = polygon(poly)
		print test_poly.area()
		print area_values[ni] == test_poly.area()

	test_poly = polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
	mz_translate_scale = np.matrix(np.array([[1,0,0,2],[0,1,0,3],[0,0,1,4],[0,0,0,2.0]]))
	mz_scale = np.matrix(np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,2.0]]))

	print test_poly.verts
	print test_poly.transform(mz_scale)
	print test_poly.transform(mz_translate_scale)


if __name__ == '__main__':
	main()
