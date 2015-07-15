import numpy as np

class polygon:

	def __init__(self, verts):
		if(self.isValid(verts)):
			self.verts = verts

	def isValid(self,verts):
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
		for ni, i in enumerate(verts[:-3]):
			for nj, j in enumerate(verts[ni+1:-2]):
				nj += ni + 1
				D = np.subtract(verts[nj+1],j)
				B = np.subtract(verts[ni+1],i)
				Binv = (-B[1], B[0])
				A = np.subtract(i,j)

				DBinv = np.dot(D,Binv)
				print nj,ni
				#if np.dot(A,Binv) == 0:
			#		print "parallel"
				if DBinv != 0:
					t2 = np.dot(A,Binv)/DBinv
					t1 = np.dot(t2*D - A, B)/np.dot(B,B)
					if nj-ni == 1: #adjacent sides
						if t2 != 0:
							print "FALSE1", t2, t1
							return False
					else:
						if (t2 >=0 and t2 <=1) and (t1 >=0 and t1 <=1) :
							print "FALSE2", t2, t1
							return False
				elif np.dot(A,Binv) == 0:
					print "?"
					return False
				else : 
					print "?"
		print "True"
		return True

def main():
	mypoly = polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
	mypoly = polygon([(-10.2, -6), (0, 0), (1, -3), (1, -7), (0, -4), (-10.2, -6)])
	invalid_polys = [[(0, 0), (1, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0.5, 1), (0.5, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0, 0), (-1, 0), (0, -1), (0, 0)],
						[(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]]
	for poly in invalid_polys:
		mypoly = polygon(poly)


if __name__ == '__main__':
	main()